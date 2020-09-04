# Remember the word Version 1
#
# Displays 4 words to users. User is prompted to recall one of
# those four words. This is the the first programming project
# in CMPUT174, Winter 2018.
import time

def main():
    # display instructions
    print('A sequence of words will be displayed.')
    print('You will be asked which word start with')
    print('a particular letter.')
    print('You win if you enter the right word.')
    response = input('Press enter key to display the words.')
        
    # present words: orange, chair, mouse, sandwich
    print('orange')
    time.sleep(2)
    print('chair')
    time.sleep(2)
    print('mouse')
    time.sleep(2)
    print('sandwich')
    time.sleep(2)
    
    # prompt user for input
    guess = input('What word begins with the letter c?')
    
    # display feedback
    print('Congratulations, you are correct.')
    print('Sorry, you entered ' + guess)
    print('The answer was chair')
    response = input('Press enter to end the game.')
    
    # terminate program
    # this will happen automatically
 
main()
