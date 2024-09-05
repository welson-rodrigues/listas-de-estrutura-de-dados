from binarytree import build

valores = [8, 5, 1, 7, 10, 12]

arvore = build(valores)

def pre_ordem(arvore):
    if arvore is None:
        return arvore
    print(arvore.value)
    pre_ordem(arvore.left)
    pre_ordem(arvore.right)

print("Árvore criada com lista")
print(arvore)
pre_ordem(arvore)