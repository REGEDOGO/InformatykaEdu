plik = open("liczby.txt")

def czy5RoznichCzynPierwszych(liczba):
    dzielniki = set()
    dzielnik = 2
    while liczba > 1:
        while liczba % dzielnik == 0:
            liczba = liczba / dzielnik
            dzielniki.add(dzielnik)
        dzielnik += 1
        if dzielnik > 3:
            dzielnik += 1
    return len(dzielniki)>=5

for linia in plik:
    liczba = int(linia.strip())
    if czy5RoznichCzynPierwszych(liczba):
        print(liczba)

