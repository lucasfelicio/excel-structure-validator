"""Módulo para validação de colunas a mais."""

from typing import Tuple

from pandas import DataFrame


def validar_se_existem_colunas_a_mais (execl_modelo: DataFrame, arquivo: DataFrame) -> Tuple[bool, str]:
    """Função para verificar se o arquivo recebido tem colunas a mais em relação ao
    modelo."""
    
    colunas_a_mais = set(arquivo.columns) - set(execl_modelo.columns)

    return len(colunas_a_mais) == 0, list(colunas_a_mais)