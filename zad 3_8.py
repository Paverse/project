def kosztzakupow(**items):
    temp1 = len(items)
    temp2 = 0
    for x in items:
        temp2 += items[x]
    print(temp1)
    print(temp2)
kosztzakupow(a = 5,b = 10,c = 15, d =20 )