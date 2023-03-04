class Czlowiek:
    def __init__(self):
        self.imie = "kamil"
        self.nazwisko = 'musial'
        self.wiek = 30
        self.wyplata = 5000
        self.ID = 12345

    def zwieksz_wyplate(self, o_ile):
        if o_ile > 0:
            self.wyplata += o_ile

    def zmien_id(self, nowe_id):
        print('sprawdzam dostepnosc nowego id')
        self.ID = nowe_id

class Data:
    def __init__(self):
        self.dzien = 1
        self.miesiac = 1
        self.rok = 1900
        self.dzien_tygodnia = 'monday'

    def dodaj_dni(self, ile):
        pass
czlowiek1 = Czlowiek()
print(czlowiek1.nazwisko)
print(czlowiek1.ID)
czlowiek1.zmien_id(987)
print(czlowiek1.ID)