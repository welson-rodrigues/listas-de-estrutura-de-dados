from binarytree import bst

no = bst(height = 4)

def buscar_6(no, valor):
    if no is None:
        print("O número 6 não foi encontrado")
        return None
    elif valor == no.value:
        print("O 6 foi encontrado")
        return no
    elif valor < no.value:
        return buscar_6(no.left, valor)
    else:
        return buscar_6(no.right, valor)

print("Árvore:")
print(no)
buscar_6(no, 6)