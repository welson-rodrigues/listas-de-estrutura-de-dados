from binarytree import bst, Node

def count_leaves(node):
    # Caso base: se o nó é None, não há folhas
    if node is None:
        return 0
    
    # Se o nó não tem filhos, ele é uma folha
    if node.left is None and node.right is None:
        return 1
    
    # Recursivamente conte as folhas nas subárvores esquerda e direita
    return count_leaves(node.left) + count_leaves(node.right)

# Exemplo de uso:
no = bst(height=4)

print("Árvore: ")
print(no)

# Contando o número de nós folha
num_folhas = count_leaves(no)
print(f"Número de nós folha: {num_folhas}")
