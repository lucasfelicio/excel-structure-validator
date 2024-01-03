"""Módulo de validação de quantidade de linhas."""

from typing import Tuple
from pandas import DataFrame

def validar_quantidade_linhas(excel_modelo: DataFrame, arquivo: DataFrame) -> Tuple[bool, str]:
    """Função para verificar se o arquivo recebido tem o mesmo número
    de linhas em relação ao modelo."""
    numero_linhas_df1 = len(excel_modelo)
    numero_linhas_df2 = len(arquivo)

    return numero_linhas_df1 == numero_linhas_df2, numero_linhas_df2 - numero_linhas_df1    