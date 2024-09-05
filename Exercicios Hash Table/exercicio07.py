produtos = {
    "P001": "Arroz",
    "P002": "Feijão",
    "P003": "Macarrão"
}

# Códigos e nomes
for codigo, nome in produtos.items():
    print(f"Código: {codigo}, Nome: {nome}")

# Códigos dos produtos
for codigo in produtos.keys():
    print(f"Código: {codigo}")

# Apenas os nomes
for nome in produtos.values():
    print(f"Nome: {nome}")
