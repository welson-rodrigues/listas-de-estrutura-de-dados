from binarytree import bst

no = bst(height=4)

def maior_valor(no):
    # Começa pela raiz
    if no is None:
        return None
    
    # Se move pela direita até não ter mais números maiores
    while no.right is not None:
        no = no.right
    return no.value

print("Árvore:")
print(no)

resultado = maior_valor(no)
print("Maior valor encontrado: ", resultado)