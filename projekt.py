#program, który sprawdzi, czy dane słowo to palindron
#progrm, który działa na liście słow

napis = "Kamil ma psa"
lista_zwierzat = ["pies", "drugi pies", 44]

print(napis[2:6])
print(lista_zwierzat[2])
print(lista_zwierzat[2][3:7])
print(lista_zwierzat[2][-3])
for i in range(20,4,-3):       #od, do, krok
    print(i)

for i in range(4):    # i jest iteratorem, mozemy użyc tak jak chcemy
    print('okrazanie ',i+1,', a litera nr ',i+4,'to',napis[i+3],'\n')

for litera in napis:
    print(litera)
for zwierze in lista_zwierzat:
    print(zwierze)





