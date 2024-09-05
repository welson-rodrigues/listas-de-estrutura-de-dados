from binarytree import bst

no = bst(height=4)

def soma(no):
    if no is None:
        return 0
    return no.value + soma(no.left) + soma(no.right)
print(no)

result = soma(no)
print("A soma de todos os nós é:", result)