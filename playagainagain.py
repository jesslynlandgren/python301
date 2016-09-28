def playAgain():

    again = raw_input("Do you want to play again? (y / n):  ")
    if again == 'y' or again == 'n':
            if again == 'y':
                return True
            else:
                return False
    else:
        print "Only enter 'y' or 'n'!"
        return playAgain()

print playAgain()
