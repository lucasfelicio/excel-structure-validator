"""Orquestrador principal do pipeline de validação de dados excel."""

import os
import shutil
import time
import pandas as pd
from loguru import logger

from src.utility.config import (INPUT_DIR, MODEL_DIR, OUTPUT_CORRETOS,
                                OUTPUT_REVISAO)
from src.validacoes import (
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
    (filename, pd.read_excel(os.path.join(INPUT_DIR,filename)))
    for filename in files_names
]

valicaoes = [
    validar_quantidade_linhas, validar_se_existem_colunas_a_mais,
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
        format='{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}'
    )
