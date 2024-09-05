from binarytree import bst

# Gerar a árvore
no = bst(height=4)

def buscar_5(no, valor):
    if no is None:
        print("5 não existe na árvore")
        return None
    elif no.value == valor:
        print("5 encontrado")
        return no
    elif valor < no.value:
        return buscar_5(no.left, valor)
    else:
        return buscar_5(no.right, valor)

def remover_no(raiz, valor):
    if raiz is None:
        return raiz
    
    if valor < raiz.value:
        raiz.left = remover_no(raiz.left, valor)
    elif valor > raiz.value:
        raiz.right = remover_no(raiz.right, valor)
    else:
        # Se não filho
        if raiz.left is None and raiz.right is None:
            return None
        # Se tiver só um filho
        elif raiz.left is None:
            return raiz.right
        elif raiz.right is None:
            return raiz.left
        # Se tiver dois filhos
        else:
            # Encontrar o sucessor (menor na subárvore direita)
            sucessor = raiz.right
            while sucessor.left is not None:
                sucessor = sucessor.left
            # Substituir o valor do nó pelo valor do sucessor
            raiz.value = sucessor.value
            # Remover o sucessor
            raiz.right = remover_no(raiz.right, sucessor.value)
    
    return raiz

print("Árvore antes da remoção:")
print(no)
buscar_5(no, 5)

no = remover_no(no, 5)

print("\nÁrvore após a remoção:")
print(no)
