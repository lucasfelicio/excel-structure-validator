"""Módulo de validação de tipos de dados."""

from typing import Tuple

from pandas import DataFrame


def validar_tipos_dados(excel_modelo: DataFrame, arquivo: DataFrame) -> Tuple[bool, str]:
    """Função para verificar se o arquivo recebido tem os mesmos tipos de dados
    em comparação ao modelo."""
    colunas_comuns = set(excel_modelo.columns).intersection(set(arquivo.columns))
    colunas_com_tipo_dados_diferentes = [col for col in colunas_comuns if excel_modelo[col].dtype != arquivo[col].dtype]
    return len(colunas_com_tipo_dados_diferentes) == 0, colunas_com_tipo_dados_diferentes