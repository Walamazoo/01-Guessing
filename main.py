import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"

quit=False

while not quit:
    guesses=0

    randomNumber=random.randint(1,100)
    print('HELLO HUMAN. I HAVE SELECTED A RADOM NUMBER BETWEEN 1 AND 100. JUST TRY AND GUESS IT!')

    guess=input()
    guess=int(guess)

    while guess!=randomNumber:
        if guess<randomNumber:
            print('HAH! OF COURSE YOU WOULD NOT GUESS HIGH ENOUGH! TRY AGAIN!')

        if guess>randomNumber:
            print('OUTLANDISH! TOO HIGH! TRY AGAIN, HUMAN!')

        guess=input()
        guess=int(guess)
        guesses=guesses+1
    if guesses<6:
        print('THAT IS CORRECT! ONLY {} TRIES? HOW COULD I HAVE BEEN SO EASILY DEFEATEEEEEEEEEED?!?!?!'.format(guesses))
    if guesses>6 and guesses<11:
        print('THAT IS CORRECT! IT TOOK YOU {} TRIES. NOT BAD.'.format(guesses))
    if guesses>10:
        print('THAT IS CORRECT! HOWEVER, {} TRIES? YOU ARE YET A MATCH FOR MY INTELLECT!'.format(guesses))
    print('SHALL WE PLAY AGAIN? (yes or no)')
    playAgain=input()
    playAgain=playAgain.lower()
    if playAgain=='yes' or playAgain=='y':
        quit=False
    else:
        quit=True
print('FAREWELL, HUMAN!')
