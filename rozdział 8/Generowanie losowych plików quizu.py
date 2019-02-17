import random, os, shelve, time

stolice = {"Alabama": "Montgomery", "Alaska": "Juneau", "Arizona": "Phoenix",
"Arkansas": "Little Rock", "Kalifornia": "Sacramento", "Kolorado": "Denver",
"Connecticut": "Hartford", "Delaware": "Dover", "Floryda": "Tallahassee",
"Georgia": "Atlanta", "Hawaje": "Honolulu", "Idaho": "Boise", "Illinois": "Springfield",
"Indiana": "Indianapolis", "Iowa": "Des Moines", "Kansas": "Topeka", "Kentucky": "Frankfort",
"Luizjana": "Baton Rouge", "Maine": "Augusta", "Maryland": "Annapolis",
"Massachusetts": "Boston", "Michigan": "Lansing", "Minnesota": "Saint Paul",
"Mississippi": "Jackson", "Missouri": "Jefferson City", "Montana": "Helena",
"Nebraska": "Lincoln", "Nevada": "Carson City", "New Hampshire": "Concord",
"New Jersey": "Trenton", "Nowy Meksyk": "Santa Fe", "Nowy Jork": "Albany",
"Karolina Północna": "Raleigh", "Dakota Północna": "Bismark", "Ohio": "Columbus",
"Oklahoma": "Oklahoma City", "Oregon": "Salem", "Pensylwania": "Harrisburg",
"Rhode Island": "Providence", "Karolina Południowa": "Columbia", "Dakota Południowa": "Pierre",
"Tennessee": "Nashville", "Teksas": "Austin", "Utah": "Salt Lake City", "Vermont": "Montpelier",
"Wirginia": "Richmond", "Waszyngton": "Olympia", "Wirginia Zachodnia": "Charleston",
"Wisconsin": "Madison", "Wyoming": "Cheyenne"}

startTime = time.time()
for quizNum in range(10):
    quizFile = open("c:\\users\\user\\desktop\\python_nauka\\q\\stolicequiz%s.txt" % (quizNum + 1),"w")
    answerKeyFile = open("c:\\users\\user\\desktop\\python_nauka\\q\\stolicequiz_odp%s.txt" % (quizNum + 1),"w")

    quizFile.write("Imię i nazwisko:\n\nData:\n\nKlasa:\n\n")
    quizFile.write(" " * 20 + "Quiz stolic USA (Quiz %s)" % (quizNum + 1))
    quizFile.write("\n\n")
    quizFile.close()
    stany = list(stolice.keys())
    random.shuffle(stany)

    for pytaniaNum in range(50):
        correctAnswer = stolice[stany[pytaniaNum]]
        wrongAnswer = list(stolice.values())
        del wrongAnswer[wrongAnswer.index(correctAnswer)]
        wrongAnswer = random.sample(wrongAnswer, 4)
        answerOptions = wrongAnswer + [correctAnswer]
        random.shuffle(answerOptions)
        quizFile = open("c:\\users\\user\\desktop\\python_nauka\\q\\stolicequiz%s.txt" % (quizNum + 1),"a")
        quizFile.write("%s. Co jest stolicą stanu %s?\n" % (pytaniaNum + 1, stany[pytaniaNum]))
        quizFile.close()
        for i in range(5):
            quizFile = open("c:\\users\\user\\desktop\\python_nauka\\q\\stolicequiz%s.txt" % (quizNum + 1),"a")
            quizFile.write("    %s. %s\n" % ("ABCDE"[i], answerOptions[i]))
            quizFile.close()
        quizFile = open("c:\\users\\user\\desktop\\python_nauka\\q\\stolicequiz%s.txt" % (quizNum + 1),"a")
        quizFile.write("\n")
        quizFile.close()
        answerKeyFile = open("c:\\users\\user\\desktop\\python_nauka\\q\\stolicequiz_odp%s.txt" % (quizNum + 1),"a")
        answerKeyFile.write("%s. %s\n" % (pytaniaNum + 1, "ABCDE"[answerOptions.index(correctAnswer)]))
        quizFile.close()
        answerKeyFile.close()
endTime = time.time()
sumTime = endTime - startTime
print("Utworzono " + str(quizNum+1) + " zestawów testów. Zajęło to " + str(round(sumTime)) + " sekund")
