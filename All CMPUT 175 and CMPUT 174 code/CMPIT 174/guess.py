# Guess the number
#
# LAB 1
# A number between 1 and 10 randomly selected 
# and user is asked to guess that number. 

import random

def main ():
    # select a random number between 1 and 10
    number = random.randint(1,10)
    print ('I am thinking of a number between 1 and 10.')
    
    # prompt user to guess a number
    guess = input('What is the number?')
    
    # Provide Feedback
    print ('The number was '+ str(number)+'.')
    print ('You guessed '+ str(guess) +'.')
    #modified code
    #print ('The number was '+ str(number)+', but you guessed '+ str(guess) +'.')
    #terminate progaram
    
main()
    
    