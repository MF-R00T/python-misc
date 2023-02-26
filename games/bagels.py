import numbers
import random

# Triple quotes ("""") is used to allow a multiple lines from a single print function  
print("""Bagels, by Al Sweigart al@inventwithpython.com

A deductive logic game where you must guess a number based on clues. View this code at https://nostarch.com/big-book-small-python-projects 
A version of this game is featured in the book Invent Your Own Computer Games with Python https://nostarch.com/inventwithpython""")

digit_len = 3 # variable setting the digit string length to guess
maxnum_guesses = 10 # variable setting out the maxinum number of guesses

def main():
    print("""Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com
I am thinking of a 3-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When I say:      That means:
Pico             One digit is correct but in the wrong position.
Fermi            One digit is correct and in the right position.
Bagels           No digit is correct.

For example, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico.""") 
    secretnum = getsecretnum()
    print("I have thought of a number")
    print("you have %d guesses to get it." % maxnum_guesses)

    numguess = 1 # variable used to stored the number of guess

    while numguess <= maxnum_guesses:
        guess = " "
        while len(guess) != digit_len or not guess.isdecimal(): # while the length of variable guess is not equal to the digit lenght 
            print("Guess #{}: ".format(numguess))
            guess = input('> ') 
    
        clues = getclues(guess,secretnum) # getclues function takes guess and secretnum variable as arguments 
        print(clues)
        numguess += 1

        if guess == secretnum:
            break # they guessed correctly so break they loop! otherwise it would run forever
        if numguess > maxnum_guesses: # if number of guesses is bigger than max allowed 
            print("You ran out of guesses")
            print("The answer was {}.".format(secretnum)) 

        print("Do you want to play again? (Yes or No)") # ask player if they want to play again
        if not input("> ").lower().startswith("y"):
            print("Thanks for playing!")      
        break
    
def getsecretnum(): #returns a string made up of digit_len unique random digits
        numbers = list("0123456789") #variable with a list of integers from 0 to 9
        random.shuffle(numbers) #shuffles in random order the numbers in variable numbers
        secretnum = ""
        for i in range(digit_len):
            secretnum += str(numbers[i])
        return secretnum

# returns the strungs with the clues after guess input and secret number pair
def getclues(guess,secretnum):
    if guess == secretnum:
        return "smart one you are! got it you did!"

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretnum[i]:
            # a correct digit in the wrong place
            clues.append("Fermi")
        if guess[i] in secretnum:
            # a correct digit in incorrect place
            clues.append("Pico")
    if len(clues) == 0:
        return "Bagels" # no correct digits at all
    else:
        #sort the clues into alphabetical order so their orginal doesn't give info away
        clues.sort()
        #make a single string from the list of string clues
        return " ".join(clues)
#if the program is run instead of imported run the game:
if __name__== '__main__':
    main()
