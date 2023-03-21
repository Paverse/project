import random
def right_triangle(a,b,c):
    przyprostokatna1 = None
    przyprostokatna2 = None
    przeciwprostokatna = None
    if a > b:
        if a > c:
            przeciwprostokatna = a
            przyprostokatna1 = b
            przyprostokatna2 = c
        else:
            przeciwprostokatna = c
            przyprostokatna1 = b
            przyprostokatna2 = a
    else:
        if b > c:
            przeciwprostokatna = b
            przyprostokatna1 = c
            przyprostokatna2 = a
        else:
            przeciwprostokatna = c
            przyprostokatna1 = b
            przyprostokatna2 = a
    if pow(przyprostokatna1,2)+ pow(przyprostokatna2,2) == pow(przeciwprostokatna,2):
        print("jest prostokatny")
    else:
        print("nie jest prostokatny")
a = None
b = None
c = None
for x in range(257):
    a = random.randint(1, 5)
    b = random.randint(1, 5)
    c = random.randint(1, 5)
    print(a,b,c)
    right_triangle(c,b,a)