from binarytree import bst, Node

def count_internal_nodes(node):
    # Caso base: se o nó é None ou é uma folha, não é um nó interno
    if node is None or (node.left is None and node.right is None):
        return 0
    
    # Se o nó tem pelo menos um filho, é um nó interno
    # Recursivamente conte os nós internos nas subárvores esquerda e direita
    return 1 + count_internal_nodes(node.left) + count_internal_nodes(node.right)

# Exemplo de uso:
no = bst(height=4)

print("Árvore: ")
print(no)

# Contando o número de nós internos
num_nos_internos = count_internal_nodes(no)
print(f"Número de nós internos: {num_nos_internos}")
