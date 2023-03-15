lista = [2,1,3,3,3,4,55,43,54,53,3,4634,2314,3,2,2,2,23,2,53,2,4,2453454,123546352466,2]
temp = 0
while temp != len(lista):
    if lista[temp] == 2:
        lista.pop(temp)
        temp -= 1
    temp += 1
print(lista)