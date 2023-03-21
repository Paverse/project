def ciag(a = 1,b = 4, ile = 10):
    ans = a
    temp = a
    for x in range(0,ile):
        temp = a * pow(b,x)
        ans *= temp
    return ans
print(ciag(1,2,5))