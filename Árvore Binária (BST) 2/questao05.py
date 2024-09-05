from binarytree import bst, Node

def level_order_traversal(root):
    if root is None:
        return []
    
    result = []
    queue = [root]  # Inicializa a fila com o nó raiz
    
    while queue:
        node = queue.pop(0)  # Remove o nó da frente da fila
        result.append(node.value)  # Adiciona o valor do nó à lista de resultados
        
        # Adiciona os filhos do nó à fila
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result

# Exemplo de uso:
no = bst(height=4)

print("Árvore: ")
print(no)

# Percorrendo a árvore em nível
resultado = level_order_traversal(no)
print(f"Sequência de nós visitados no percurso em nível: {resultado}")
