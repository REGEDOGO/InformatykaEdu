for i in (1,2,3,4,5,6,7,8,9,10):
    print(i, end=", ")

ilosc = int(input("podaj ile razy ma sie wykonac petla: "))
for i in range(ilosc):
    print("lezy ",i++1, "skibidi")

for i in range(5, 5+ilosc, 2): #range(od, do, co ile)
    print("co do sigmy nr.", i)

liczby = 5
print("zaraz mnie coś ")
while liczby > 5:
    print("*")
    liczby -= 1