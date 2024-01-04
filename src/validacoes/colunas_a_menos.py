"""Módulo para validação de colunas a menos."""

from typing import Tuple

from pandas import DataFrame


def validar_se_existem_colunas_a_menos(execl_modelo: DataFrame, arquivo: DataFrame) -> Tuple[bool, str]:
    """Função para verificar se o arquivo recebido tem colunas a menos em relação
    modelo."""
    
    colunas_a_menos = set(execl_modelo.columns) - set(arquivo.columns)

    return len(colunas_a_menos) == 0, list(colunas_a_menos)