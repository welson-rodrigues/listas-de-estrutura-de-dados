from binarytree import Node, bst

no = bst(height = 4)

def pre_ordem(no):
    if no is None:
        return
    print(no.value) # Visitação
    pre_ordem(no.left) # Esquerda
    pre_ordem(no.right) # Direita

print("Pré Ordem:")
print(no)

print("Ordem:")
pre_ordem(no)