plik = open("dane.txt")

dane = plik.read()
print(type(plik))
print(type(dane))
print(dane)
print("------")
for znak in dane:
    print(znak)

plik.seek(0)

dane = plik.readlines()
print(type(plik))
print(type(dane))
print(dane)
print("------")
for linia in dane:
    print(linia)