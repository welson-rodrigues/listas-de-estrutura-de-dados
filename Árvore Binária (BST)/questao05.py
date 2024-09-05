from binarytree import bst, Node

no = bst(height = 4)

def pos_ordem(no):
    if no is None:
        return
    pos_ordem(no.left) # Esquerda
    pos_ordem(no.right) # Direita
    print(no.value) # Visitação

print("Pós ordem", no)
pos_ordem(no)