def potegowanie(a,ile):
    ans = 1
    if ile == 0:
        return 1
    for x in range(0,ile):
        ans *= a
    return ans

def ciag(a = 1,b = 4, ile = 10):
    ans = a
    temp = a
    for x in range(0,ile):
        temp = a * potegowanie(b,x)
        ans *= temp
    return ans
print(ciag(1,2,5))