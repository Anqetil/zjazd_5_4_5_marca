#program, który sprawdzi, czy dane słowo to palindron
#progrm, który działa na liście słow

slowo = input('Wpisz slowo ')
liczba_iteracji = len(slowo)//2
for i in range (liczba_iteracji):

    print(slowo[len(slowo)-1])

