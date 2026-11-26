"""Cálculo simplificado de produção de leite para a investigação acadêmica."""


def calcular_total_diario(ordenhas, propriedade_id):
    """Soma os litros das ordenhas confirmadas da propriedade indicada."""
    return sum(
        ordenha["litros"]
        for ordenha in ordenhas
        if ordenha["propriedade_id"] == propriedade_id
        and ordenha["status"] == "confirmada"
    )
