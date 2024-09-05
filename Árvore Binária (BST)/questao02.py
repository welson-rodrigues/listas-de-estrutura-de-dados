from binarytree import bst, Node

no = bst(height = 4)

def inserir(no, valor):
    if no is None:
        return Node(valor)
    if valor < no.value:
        no.left = inserir(no.left, valor)
    else:
        no.right = inserir(no.right, valor)
    return no

no = inserir(no, 5)
no = inserir(no, 2)

print("Árvore com 5 e 2 adicionados:")
print(no)