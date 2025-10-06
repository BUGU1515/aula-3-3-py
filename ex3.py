valores = [
    10,
    3 + 2j,
    "j",
    True,
    [1, 3],
    1.2,
    None,
    (1, 2),
    {1, 2},
    {"chave": "valor", "idade": 25}
]

for valor in valores:
    print(f"Valor: {valor} - Tipo: {type(valor)}")
