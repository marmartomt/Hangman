'''
Hangman
    _________
    |         |
    |         O
    |        /|\
    |        / \
    |
    |
______________
Developers
-Brandon
-Thomas
______________
v0.1
-
'''
#declare variables
correctCharacters = []

#print Hangman function
def printhang(stage):
    if stage == 0:
        print(" _________")
        print("|         |")
        print("|         ")
        print("|        ")
        print("|        ")
        print("|")
        print("|")
        print("____")
        print ("")
    if stage == 1:
        print(" _________")
        print("|         |")
        print("|         0")
        print("|         ")
        print("|         ")
        print("|")
        print("____")
        print ("")
    if stage == 2:
        print(" _________")
        print("|         |")
        print("|         0")
        print("|        /")
        print("|        ")
        print("|")
        print("|")
        print("____")
        print ("")
    if stage == 3:
        print(" _________")
        print("|         |")
        print("|         0")
        print("|        /| ")
        print("|        ")
        print("|")
        print("|")
        print("____")
        print ("")
    if stage == 4:
        print(" _________")
        print("|         |")
        print("|         0")
        print("|        /|\ ")
        print("|         ")
        print("|")
        print("|")
        print("____")
        print ("")
    if stage == 5:
        print(" _________")
        print("|         |")
        print("|         0")
        print("|        /|\ ")
        print("|        /  ")
        print("|")
        print("|")
        print("____")
        print ("")
    if stage == 6:
        print(" _________")
        print("|         |")
        print("|         0")
        print("|        /|\ ")
        print("|        / \ ")
        print("|")
        print("|")
        print("____")
        print ("")

#Fancy intro sequence
print('''_  _ ____ _  _ ____ _  _ ____ _  _
|__| |__| |\ | | __ |\/| |__| |\ |
|  | |  | | \| |__] |  | |  | | \|''')
import time
time.sleep(1)
#restarts program
restart = 1
#checks for restart
if restart != "x":
    #prints blank lines
    for o in range(100):
        print("")

    #Asks user 1 to enter a word
    isGood = False
    while isGood == False:
        word = str(input("Player one, enter a word or phrase, under 20 characters. "))
        if len(word) <= 20:
            isGood = True

        else:
            print("Too Long! Keep it under 20 characters!")
    #prints blank lines
    for o in range(100):
        print("")
    print("Word accepted.")
    #main game loop
    win = False
    phase = 0
    while win == False:
        printhang(phase)
        blanks = ""
        for character in word:
            if character != " ":
                if blanks == "":
                    blanks = "_" + ","
                else:
                    blanks += "_" + ","
            else:
                blanks += ' '
        print(blanks)
        isGood = False
        while isGood == False:
            guess = str(input("Player two, guess a letter or the word. "))
            if len(guess) <= 20:
                isGood = True
            else:
                print("Too Long! Keep it under 20 characters!")
        correct = False
        for character in word:
            if character == guess:
                print("Correct!")
                correctCharacters.append(guess)
                correct = True
                break
        if correct == False:
            print("Incorrect!")
            phase += 1




'''
#find letter in string
    if  string.find(letter) == !number!:
        print("Correct Guess!")
        #removes letter from Word, shows letters left in the word
        print("letters left",len(string) - 1)
'''





#"input("Press x to close")"
