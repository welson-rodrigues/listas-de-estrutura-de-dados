from binarytree import bst, Node

def is_balanced(node):
    # Função auxiliar para calcular a altura de uma subárvore
    def height(node):
        if node is None:
            return 0
        return max(height(node.left), height(node.right)) + 1
    
    # Caso base: uma árvore vazia é balanceada
    if node is None:
        return True
    
    # Calcular a altura das subárvores esquerda e direita
    left_height = height(node.left)
    right_height = height(node.right)
    
    # Verificar a condição de balanceamento para o nó atual
    if abs(left_height - right_height) > 1:
        return False
    
    # Recursivamente verificar as subárvores esquerda e direita
    return is_balanced(node.left) and is_balanced(node.right)

# Exemplo de uso:
no = bst(height=4)

print("Árvore: ")
print(no)

# Verificando se a árvore está balanceada em termos de altura
resultado = is_balanced(no)
print(f"A árvore está balanceada? {resultado}")
