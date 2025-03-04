n = 179
w = 4
k = 5

binarna = ""
dl = 0

while n > 0:
    if n%2 == 0:
        binarna = '0'+binarna
    else:
        binarna = '1'+binarna
    dl+=1
    n = n//2

print(binarna, dl)
miejsc = w*k
reszta = miejsc % dl

print(reszta)
if reszta > 0:
    print(binarna[reszta-1])
else:
    print(binarna[reszta])

# zad 2
wyw = 0

def F(x):
    global wyw
    wyw += 1
    if x == 0:
        return 0
    else:
        return 2+F(x//2)

print(F(3), wyw)
wyw = 0
print(F(16), wyw)
wyw = 0
print(F(35), wyw)
wyw = 0

for x in range(100):
    print(x, F(x), sep="->")
