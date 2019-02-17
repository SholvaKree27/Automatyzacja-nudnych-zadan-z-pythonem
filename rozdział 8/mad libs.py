#Moja propozycja rozwiązania Projektu praktycznego z rozdziału 8: Program Mad Libs. 
#W zadaniu jest błąd, gdyż w wytycznych jest zamiana przymiotnik, rzeczownik, czasownik i przysłówek. W "program powinen...", zamiast
# przysłówka jest drugi raz rzeczownik. Co mnie zmyliło i tym samym napisałem taki, a nie inny kod. Choć lepsze rozwiązanie znajdziecie u 
# https://github.com/IFinners/automate-the-boring-stuff-projects/blob/master/Chapter%2008/mad_libs.py

# podajemy nowe wartości, dla słów, które zostaną podmienione
przymiotnik_new = input("Podaj przymiotnik: ")
rzeczownik_new = input("Podaj rzeczownik: ")
czasownik_new = input("Podaj czasownik: ")
rzeczownik_2_new = input("Podaj rzeczownik: ")

#otwieramy plik
file = open("c:\\users\\user\\desktop\\python_nauka\\mad_lips.txt")
find = file.readline()

#po koleji zamieniamy wartości
przymiotnik_re = find.replace("PRZYMIOTNIK",str(przymiotnik_new))
rzeczownik_re = przymiotnik_re.replace("RZECZOWNIK",str(rzeczownik_new), 1) #tak jak wspominałem, myślałem, że są dwa rzeczowniku, tutaj zamieniamy pierwszy
czasownik_re = rzeczownik_re.replace("CZASOWNIK",str(czasownik_new))
rzeczownik_2_re = czasownik_re.replace("RZECZOWNIK",str(rzeczownik_2_new))
text = rzeczownik_2_re

file.close()

print(text)

#tutaj następuje podmiana wartości w pliku
file = open("c:\\users\\user\\desktop\\python_nauka\\mad_lips.txt", "w")
file.write(text)
file.close()
