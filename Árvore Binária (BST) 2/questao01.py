from binarytree import bst, Node

def e_bst(node, min_value=float('-inf'), max_value=float('inf')):
    # Caso base: uma árvore vazia é uma BST válida
    if node is None:
        return True
    
    # Verifique se o valor do nó atual está dentro do intervalo permitido
    if not (min_value < node.value < max_value):
        return False
    
    # Recursivamente verifique as subárvores esquerda e direita
    return (e_bst(node.left, min_value, node.value) and
            e_bst(node.right, node.value, max_value))

# Exemplo de uso:
no = bst(height=4)

print("Árvore: ")
print(no)

# Verificando se a árvore é uma BST
resultado = e_bst(no)
print(f"A árvore é uma BST? {resultado}")
