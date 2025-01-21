import math

file = open("../zad3/liczby_przyklad.txt")

def isSquareFullNumber(num):
    pier = math.sqrt(num)
    full = int(pier)
    return full == pier

potegi = []
p = 1
while 1:
    potega = p**2
    if potega >= 100 and potega <= 9999:
        potegi.append(potega)
    p+=1
    if potega > 9999:
        break

print(potegi)

licznik = 0
first = 0
for row in file:
    num = int(row.strip())
    if num in potegi:
        licznik+=1
        if first == 0:
            first = num
print(licznik, first)