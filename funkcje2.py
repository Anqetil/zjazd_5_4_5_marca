import time

def welcome_basic():
    time.sleep(0.5)
    print('przygotowanie obrazu sygnalu')
    time.sleep(0.5)
    print('sprawdzanie bledow w systemie')
    time.sleep(0.5)
    print('Siema')

welcome_basic()


def welcome_full(imie, wiek):
    if wiek >= 18:
        print('Dzien dobry', imie)
    else:
        print('Czesc', imie)

def stan_zdrowia(waga, wzrost):
    BMI = waga / (wzrost**2)
    return BMI

