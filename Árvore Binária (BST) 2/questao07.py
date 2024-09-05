from binarytree import bst

def has_path_sum(root, sum):
    if not root:
        return False

    if not root.left and not root.right and root.val == alvo:
        return True

    return has_path_sum(root.left, alvo - root.val) or \
           has_path_sum(root.right, alvo - root.val)

# Criando uma árvore BST aleatória
my_tree = bst(height=4)
print(my_tree)

# Definindo o valor alvo
alvo = 15

# Verificando se existe um caminho com a soma alvo
if has_path_sum(my_tree, target_sum):
    print(f"Existe um caminho com a soma {alvo} na árvore.")
else:
    print(f"Não existe um caminho com a soma {alvo} na árvore.")