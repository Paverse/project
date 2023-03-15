a = int(input('podaj a'))
b = int(input('podaj b'))
list = [2,1,3,3,7,5,9,23,52536458,35647,365,637563426,753,6457,6432564,325,645,362,7456,43]
if a == b:
    print('liczby sa rowne')
else:
    print('liczby sa rozne')
for x in range(1,6,1):
    print(x)
for x in range(len(list)):
    print(list[x])
temp = 0
while temp != len(list):
    print(list[temp])
    temp += 1
