from producao import calcular_total_diario


ordenhas = [
    {"propriedade_id": 1, "litros": 80, "status": "confirmada"},
    {"propriedade_id": 1, "litros": 20, "status": "cancelada"},
    {"propriedade_id": 2, "litros": 35, "status": "confirmada"},
]

print("Total da propriedade 1:", calcular_total_diario(ordenhas, 1), "L")
print("Resultado esperado: 80 L")
