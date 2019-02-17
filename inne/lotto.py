#Program do generowania 6 cyfr z przedziału 1-49.
import random
import os
import sys

def losowanie():
    for i in range (1, 7):
        number = random.randint(1, 49)
        while number in lotteryNumbers:
            number = random.randint(1, 49)
        lotteryNumbers.append(number)
    lotteryNumbers.sort()
def kupon():
    while len(user_numery) < 6:
        numery = int(input("Podaj liczbę z zakresu od 1 do 49: "))
        while numery < 1 or numery > 49:
            numery = int(input(f"Podaj liczbę z zakresu od 1 do 49!!! "))
            os.system("cls")
        os.system("cls")

        if numery not in user_numery:
            user_numery.append(numery)
            if len(user_numery) < 6:
                print("Podałaj jeszcze " + str(6-int(len(user_numery))) + ".")
            else:
                os.system("cls")
        elif numery in user_numery:
            print("Podałeś już tę cyfrę! Podaj inną.")

        user_numery.sort()

def wygrana():
    if len(trafione) == 3:
        print("Wygrałeś 5 zł!")
    elif len(trafione) == 4:
        print("Wygrałeś 100 zł!")
    elif len(trafione) == 5:
        print("Wygrałeś 5000 zł")
    elif len(trafione) == 6:
        print("Wygrałeś 1000000 zł!!!")
    else:
        print("Nic wygrałeś!")
        print()
def jakie_trafienia():
    for i in lotteryNumbers:
        if i in user_numery:
            trafione.append(i)

while True:
    try:
        lotteryNumbers = []
        user_numery = []
        trafione = []

        losowanie()
        kupon()
        print(f"Szczęśliwe liczby to: {lotteryNumbers}")
        print()
        print(f"Twoje liczby to: {user_numery}")
        print()
        jakie_trafienia()
        if len(trafione) != 0:
            print("Udało Ci się trafić " + str(len(trafione)) + " razy. Trafione cyfry to: " + str(trafione))
        print()
        wygrana()

    except ValueError:
        print("Tylko cyfry! To nie Koło Fortuny!")
        print()
    print("Wpisz 'exit' jeśli chcesz wyjść z programu. W innym przypadku naciśnij enter: ")
    response = input(">>> ").upper()
    if response == "EXIT":
        sys.exit()
