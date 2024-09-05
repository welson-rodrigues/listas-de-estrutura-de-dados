# Exercício 1

# Criação de dicionário
alunos = {}

# Adicionando os elementos
alunos["João"] = 8.5
alunos["Maria"] = 9.0
alunos["Pedro"] = 7.5
alunos["Ana"] = 8.7 # Ana adicionada

# Mostrando a nota de Maria
#print("Nota de Maria: ", alunos["Maria"]) # Saída: 9.0

# Exercício 2

# Atualizando a nota de Pedro
del alunos["Pedro"] # Removendo a nota 7.5
alunos["Pedro"] = 8.0 # Adicionando a nota 8.0

# Exercício 3

# Removendo o aluno João
del alunos["João"]

# Exercício 4
contador = 0
for chave, valor in alunos.items():
    contador = contador + 1
    print(chave, valor)
print("João" in alunos) # Saída: False

# Exercício 5

# Verificando se Ana está no dicionário
print("Ana" in alunos) # Saída: False

# Exercício 6

# Número total de alunos
print(f"Número de alunos: {contador}")
