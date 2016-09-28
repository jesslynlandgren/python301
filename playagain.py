def playAgain():
    again = raw_input("Do you want to play again? (y / n):  ")
    if again == 'y':
        return True
    else:
        return False

print playAgain()
