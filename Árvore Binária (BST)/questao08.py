from binarytree import bst

no = bst(height=4)

def menor_valor(no):
    # Começa pela raiz
    if no is None:
        return None
    
    # Fica se movendo pra esquerda até não ter mais números menores
    while no.left is not None:
        no = no.left
    return no.value

print("Árvore:")
print(no)

resultado = menor_valor(no)
print("Menor valor encontrado: ", resultado)