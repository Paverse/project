import random
a = random.randint(0,15)
lista = []
for x in range(a):
    lista.append(random.randint(0,30))
b = random.randint(0,15)
for x in range (b):
    lista.append(random.uniform(0,30))
for i in range(len(lista)):
    lista[i] *= lista[i]
print(lista)



