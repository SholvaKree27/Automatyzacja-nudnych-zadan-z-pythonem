#Program na podstawie nr PESEL wyciąga dane o użytkowniku

import sys

while True:
    try:
        pesel = input("Podaj nr PESEL: ")
        lista = []
        for i in range(len(pesel)):
            lista.append(int(pesel[i]))
    except ValueError:
        print("Nr PESEL to cyfry!")
    print()
    def plec():
        global plec1
        if lista[9] % 2 == 0:
            plec1 = "kobietą"
        else:
            plec1 = "mężczyzną"

    def poprawnosc():
        wartosc1 = lista[0] * 9 + lista[1] * 7 + lista[2] * 3 + lista[3] * 1 + lista[4] * 9 + lista[5] * 7 + lista[6] * 3 + lista[7] * 1 + lista[8] * 9 + lista[9] * 7
        global test_poprawnosci
        wartosc2 = wartosc1 % 10
        if wartosc2 == lista[10]:
            test_poprawnosci = True
        else:
            test_poprawnosci = False

    def test_wieku():
        global wiek
        x1 = int(lista[0])
        x2 = int(lista[1])
        x3 = int(str(x1) + str(x2))
        if lista[2] == 0 or lista[2] == 1:
            x4 = 1900 + x3
        elif lista[2] == 2 or lista[2] == 3:
            x4 = 2000 + x3
        elif lista[2] == 8 or lista[2] == 9:
            x4 = 1800 + x3
        wiek = 2019 - x4

    if len(pesel) == 11:
        poprawnosc()
        plec()
        test_wieku()
        
        if test_poprawnosci == True:

            print("Jesteś " + str(plec1) + " i masz " + str(wiek) + " lat.")

        else:
            print("Nie wiem co to za ciąg znaków, ale nie jest to nr PESEL!")
    else:
        print("Nr PESEL musi zawierać 11 cyfr!")

    print()
    print("Wpisz 'exit' jeśli chcesz wyjść z programu. W innym przypadku naciśnij enter: ")
    response = input(">>> ").upper()
    if response == "EXIT":
        sys.exit()
