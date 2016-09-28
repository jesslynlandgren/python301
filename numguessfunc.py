import random

def guessNum():
    print 'GUESS A NUMBER GAME:\n'
    play = True
    while play
        play = play()

def play(play):
    print 'I am thinking of a number between 1 and 10.'
    guessNum = 5
    num = getNum()
    guess = getGuess()
    whereGuess(num, guess)

    play = playagain()

    printGuessLeft(guessnum)

def getNum():
    return random.randint(1,10)

def getGuess():
    return int(raw_input("What's the number? "))

def whereGuess(num,guess,guessnum):

    if guessCorrect(num,guess):


    elif guess > num:
        print str(guess) + ' is too high.\n'
        numguess -= 1
        continue

    else:
        print str(guess) + ' is too low.\n'
        numguess -= 1
        continue

def guessCorrect(num,guess):
    if num == guess:
        return True
    else
        return False

def printGuessLeft(numguess):
    s = 's' if numguess == 1 else s='s'
    print 'You have {0} guess{1} left'.format(numguess,s)


def playAgain():
    again = raw_input("Do you want to play again? (y / n):  ")
    if again not 'y' or 'n':
        return False
    else:
        print "Only enter 'y' or 'n'!"
        playAgain()


guessNum()
