transacoes = [("joao", 100), ("maria", 200), ("joao", 300), ("maria", 150)]

somar = {}

for nome, valor in transacoes:
    if nome in somar:
        somar[nome] += valor
    else:
        somar[nome] = valor

print(somar)
