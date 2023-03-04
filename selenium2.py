czlowiek1 = ['kamil, musial', 34, 'm', 2, 3500]
czlowiek2 = ['andy, adolf', 54, 'k', 1, 3100]

czlowiek2[4] = 3
print(czlowiek2)

def zwieksz_wyplate(wyplata, zwieksz):
    return wyplata + zwieksz

czlowiek1[5] = zwieksz_wyplate(czlowiek2)
print(czlowiek1)