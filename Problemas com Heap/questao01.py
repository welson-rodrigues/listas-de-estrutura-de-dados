import random
import heapq

numeros_aleatorios = [random.randint(1, 10000) for _ in range(1000)]

numeros_menores = heapq.nsmallest(10, numeros_aleatorios)

print(numeros_aleatorios)
print("Os 5 menores números:", numeros_menores)