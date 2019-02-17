import os

przymiotnik_new = input("Podaj przymiotnik: ")
rzeczownik_new = input("Podaj rzeczownik: ")
czasownik_new = input("Podaj czasownik: ")
rzeczownik_2_new = input("Podaj rzeczownik: ")

file = open("c:\\users\\user\\desktop\\python_nauka\\mad_lips.txt")
find = file.readline()

przymiotnik_re = find.replace("PRZYMIOTNIK",str(przymiotnik_new))
rzeczownik_re = przymiotnik_re.replace("RZECZOWNIK",str(rzeczownik_new), 1)
czasownik_re = rzeczownik_re.replace("CZASOWNIK",str(czasownik_new))
rzeczownik_2_re = czasownik_re.replace("RZECZOWNIK",str(rzeczownik_2_new))
text = rzeczownik_2_re

file.close()

print(text)

file = open("c:\\users\\user\\desktop\\python_nauka\\mad_lips.txt", "w")
file.write(text)
file.close()
