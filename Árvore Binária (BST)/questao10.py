from binarytree import bst

no = bst(height=4)

def altura(no):
    if no is None:
        return -1  # Altura de uma árvore vazia é -1

    altura_esquerda = altura(no.left)
    altura_direita = altura(no.right)

    # A altura do nó atual é o maior valor entre as alturas das subárvores + 1
    return max(altura_esquerda, altura_direita) + 1

print("Árvore:")
print(no)

print("Altura da árvore:", altura(no))
