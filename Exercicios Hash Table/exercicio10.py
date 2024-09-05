palavras = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]
contagem = {}

for palavra in palavras:
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1

print(contagem)
