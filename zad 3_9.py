import math
def pierwiastek(a):
    try:
        temp = math.sqrt(a)
    except ValueError:
        print("skill issue")
    else:
        return temp
print(pierwiastek(4))