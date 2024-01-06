"""Módulo de validação de colunas na ordem."""

from typing import Tuple

from pandas import DataFrame


def validar_se_todas_as_colunas_estao_presentes_na_mesma_ordem(
    excel_modelo: DataFrame, arquivo: DataFrame
) -> Tuple[bool, str]:
    """Função para verificar se todas as colunas do modelo estão na mesma ordem
    em relação ao arquivo recebido."""
    if excel_modelo.columns.equals(arquivo.columns):
        return True, "Todas as colunas estão presentes na mesma ordem."
    else:
        return False, "Algumas colunas não estão presentes na mesma ordem."
