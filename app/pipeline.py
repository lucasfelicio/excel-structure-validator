"""Orquestrador principal do pipeline de validação de dados excel."""

import os
import shutil
import time
import pandas as pd
from loguru import logger

from .config import (INPUT_DIR, MODEL_DIR, OUTPUT_CORRETOS,
                                OUTPUT_REVISAO)
from .validacoes import (
    validar_quantidade_linhas, validar_se_existem_colunas_a_mais,
    validar_se_existem_colunas_a_menos,
    validar_se_todas_as_colunas_estao_presentes,
    validar_se_todas_as_colunas_estao_presentes_na_mesma_ordem,
    validar_tipos_dados)

excel_modelo = pd.read_excel(f'{MODEL_DIR}')

files_names = []

for filename in os.listdir(INPUT_DIR):
    if filename.endswith('.xlsx'):
        files_names.append(filename)

files_names.sort()

arquivos_recebidos = [
    (filename, pd.read_excel(os.path.join(INPUT_DIR, filename)))
    for filename in files_names
]

valicaoes = [
    validar_se_existem_colunas_a_mais,
    validar_se_existem_colunas_a_menos,
    validar_se_todas_as_colunas_estao_presentes,
    validar_se_todas_as_colunas_estao_presentes_na_mesma_ordem,
    validar_tipos_dados
]

for i, (filename, arquivo) in enumerate(arquivos_recebidos, start=1):
    
    log_file_name = f'auditoria:{filename[:-5]}-data:{time.strftime("%Y-%m-%d")}.log'

    logger.remove()
    logger.add(
        log_file_name, 
        level='INFO',
        format='{time:YYYY-MM-DDTHH} | {level} | {message}'
    )

    logger.info(f'Iniciando o proceso de validação {filename}.')
    
    resultados = []
    testes_falhos = []

    for idx, validacao in enumerate(valicaoes, start=1):
        
        resultado, msg = validacao(excel_modelo, arquivo)
        
        if resultado:
            logger.info(f'Arquivo {filename} - Teste {idx}.{validacao.__name__}: {msg}')
        else:
            logger.error(f'Arquivo {filename} - Teste {idx}.{validacao.__name__}: {msg}')
            testes_falhos.append(idx)
        
        resultados.append(resultado)
    
    origem_excel = os.path.join(INPUT_DIR, filename)
    origem_log = (
        log_file_name
    )

    if all(resultados):
        
        logger.info(f'Todos os testes passaram.')
        
        destino_excel = os.path.join(OUTPUT_CORRETOS, filename)
        destino_log = os.path.join(OUTPUT_CORRETOS, log_file_name)

        shutil.move(origem_excel, destino_excel)
        shutil.move(origem_log, destino_log)
    else:
        testes_falhos_str = ', '.join(map(str, testes_falhos))
        logger.critical(f'Arquivo {filename} - Teste(s) {testes_falhos_str} falhou(ram).')
        
        destino_excel = os.path.join(OUTPUT_REVISAO, filename)
        destino_log = os.path.join(OUTPUT_REVISAO, log_file_name)

        shutil.move(origem_excel, destino_excel)
        shutil.move(origem_log, destino_log)