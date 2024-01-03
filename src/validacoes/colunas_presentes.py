"""Módulo de validação de colunas presentes."""

from typing import Tuple
from pandas import DataFrame

def validar_se_todas_as_colunas_estao_presentes(
    excel_modelo: DataFrame, arquivo: DataFrame
) -> Tuple[bool, str]:
    """Função para verificar se todas as colunas do modelo existem no arquivo."""
    if set(excel_modelo.columns) == set(arquivo.columns):
        return True, "Todas as colunas estão presetes."
    else:
        return False, "Algumas colunas não estão presentes."