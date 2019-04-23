# This program is creating tests with countries and their capitals and also file with correct answers for each of them.
import random

test_quantity =int(input('How many test(s) would you like to create ?: '))              # Estabilishing number of tests

# Creating data with countries (keys) and  their capitals (values)
capitals = {'Albania':'Tirana','England':'London', 'Austria':'Vienna', 'Belgium':'Brussels','Belarus':'Minsk','Bosnia and Herzegovina':'Sarajevo',
            'Bulgaria':'Sofia', 'Croatia':'Zagreb', 'Montenegro':'Podgorlica', 'Czech Republic':'Prague', 'Denmark':'Copenhagen', 'Estonia':'Tallinn',
            'Finland':'Helsinki', 'France':'Paris', 'Greece':'Athens', 'Spain':'Madrid', 'Netherlands':'Amsterdam', 'Ireland':'Dublin',
            'Northern Ireland':'Belfast', 'Iceland':'Reykjavik', 'Liechtenstein':'Vaduz', 'Lithuania':'Vilnius','Luxembourg':'Luxembourg',
            'Latvia':'Riga', 'Macedonia':'Skopje', 'Malta':'Valetta', 'Monaco':'Monaco','Germany':'Belin', 'Norway':'Oslo', 'Poland':'Warsaw',
            'Portugal':'Lisbon', 'Russia':'Moscow','Romania':'Bucharest', 'Slovenia':'Ljubljana','Serbia':'Belgrade', 'Scotland':'Edinburgh',
            'Switzerland':'Bern', 'Sweden':'Stockholm', 'Turkey':'Ankara','Ukraine':'Kiev', 'Wales':'Cardiff', 'Hungary':'Budapest',
            'Italy':'Rome', 'Vatican':'Vatican'}

for quizNum in range(test_quantity):                                                    # Creating tests
    quizFile = open('capitalsquiz%s.txt' % (quizNum+1), 'w')                            # Creating file with questions
    answerKeyFile = open('capitalsquiz_answers%s.txt' % (quizNum + 1), 'w')             # Creating file with answers

    quizFile.write('Name and surname:\n\nData:\n\nClass:\n\n')                          # Adding text to every file with name, surname and class number
    quizFile.write((' ' * 20) + 'Capitals quiz set no. %s' % (quizNum+1))               # 20 spacebars and tittle
    quizFile.write('\n\n')                                                              # 2 new lines

    countries = list(capitals.keys())                                                   # Creating a list with keys (countries)
    random.shuffle(countries)                                                           # Changing index numbers in list of each country

    for questionNum in range(len(countries)):                                           # Loop which create questions with answers of every country from list
        correctAnswer = capitals[countries[questionNum]]                                # Variable with correct answer for every question
        wrongAnswers = list(capitals.values())                                          # Creating list with wrong answers but there is correct answer in it
        del wrongAnswers[wrongAnswers.index(correctAnswer)]                             # Deleting a correct answer from list
        wrongAnswers = random.sample(wrongAnswers, 3)                                   # Creating list with random 3 wrong answers
        answerOptions = wrongAnswers + [correctAnswer]                                  # Creating 4 options to choose
        random.shuffle(answerOptions)                                                   # Changing index of answers
        quizFile.write('%s. What is a capital of %s ? \n' % (questionNum + 1, countries[questionNum]))  #Adding text for every question
        for i in range(4):                                                              # Loop with answers A,B,C or D
            quizFile.write('    %s. %s\n' % ('ABCD'[i], answerOptions[i]))              # Adding 'A', 'B', 'C' or 'D' to every answer
            quizFile.write('\n')                                                        # New line
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)])) # Adding correct answer option to answerKeyFile file
    quizFile.close()                                                                    # Closing file with quiz
    answerKeyFile.close()                                                               # Closing file with answers