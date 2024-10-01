plik = open("liczby.txt")

dane = plik.readlines()
tab = list()

for liczba in dane:
    liczba = int(liczba.strip())
    tab.append(liczba)

print("max: ", max(tab), ", min: ", min(tab))
# True pisane z dużej litery
sortedTab = sorted(tab, reverse=True)
print(sortedTab)

sprawdzaj = 33

if sprawdzaj in tab:
    print(sprawdzaj, "JEST ", tab.count(sprawdzaj), " razy w zbiorze")
else:
    print(sprawdzaj, "NIE jest w zbiorze")

#czas na samo zadanie:
for liczba in tab:
    # zbiory (set) przechowują tylko niepowtarzające się wartości
    zbior = set()
    dzielnik = 2
    while liczba != 1:
        if liczba % dzielnik == 0:
            liczba /= dzielnik
            zbior.add(dzielnik)
        else:
            dzielnik += 1
    #tutaj dokończymy za tydzień