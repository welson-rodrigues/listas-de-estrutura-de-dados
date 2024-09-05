from binarytree import Node, bst

no = bst(height = 4)

def em_ordem(no):
    if no is None:
        return
    em_ordem(no.left) # Esquerda
    print(no.value) # Visitação
    em_ordem(no.right) # Direita

print("Em ordem:", no)
em_ordem(no)