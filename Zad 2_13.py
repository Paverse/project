import math
lista = []
temp = None
for x in range(10):
    temp = int(input("input value"))
    if math.fmod(temp, 2) == 0:
        lista.append(temp)
print(lista)