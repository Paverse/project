import random
lista = []
for x in range(10):
    lista.append(random.randint(0, 256))
lista2 = [x for x in lista if x % 2 == 0]
print(lista2)