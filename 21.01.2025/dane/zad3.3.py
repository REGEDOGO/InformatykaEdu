plik = open("liczby.txt")

def roznica(liczba):
    cyfry = []
    for znak in str(liczba):
        cyfry.append(znak)
        najmniejsza = int("".joinsorted(cyfry))
        najwieksza = int(sorted(cyfry, reverse = True))
    return najwieksza - najmniejsza

wieksze = mniejsze = rowne = 0
rownaliczba = 0

for linia in plik:
    liczba = int(linia.strip())
    roz = roznica(liczba)
    if roz > liczba:
        wieksze += 1
    elif roz < liczba:
        mniejsze += 1
    else:
        rowne += 1
        rownaliczba = liczba