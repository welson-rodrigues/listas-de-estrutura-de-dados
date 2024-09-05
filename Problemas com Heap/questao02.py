import random
import heapq

precos = [random.uniform(1, 10000) for _ in range(20)]

"""UMA FORMA DE FAZER"""
#k = 5
#maiores_precos = heapq.nlargest(k, precos)

#print(precos)
#print("Os 5 maiores preços:", maiores_precos)


"""OUTRA FORMA DE FAZER"""
for n in range(len(precos)):
    precos[n] *= -1 
print('Sem heapq: ', precos)
heapq.heapify(precos)

print('Com heapq: ', precos)

for k in range(len(precos)):
    precos[k] *= -1 
print("Os números em ordem do maior para o menor:", precos)

print("Os cincos primeiros maiores números:")
for a in range(5):
    print(precos[a])
