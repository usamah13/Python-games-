from random import randint
def isInputValid(input):
    if (input >= 1 and input <= 20):
        return True
    else:
        return False

def main():
    NUMBER_OF_ATTEMPTS = 4
    
    play = input("Do you want to play the number guessing game ? Y/N : ")
    
    while (play == "Y" or play == "y"):
        answer = randint(1, 21)
        attempts = 1
        print("*** Number Guessing Game Starts *** ")
        while (attempts <= NUMBER_OF_ATTEMPTS):
            guess = int(input("Enter a guess [1-­‐20]: "))
            if (isInputValid(guess)):
                if (guess < answer):
                    print("Too low!")
                    attempts += 1
                elif(guess > answer):
                    print("Too high!")
                    attempts += 1
                else:
                    print("Correct! The number was " + str(answer) + ".")
                    attempts = 5 # break loop
            else:
                print("That number is not between 1 and 20!")
        if (guess != answer):
            print("You are out of guesses. The number was " + str(answer) + ".")
        print("*** Number Guessing Game Ends ***")
        play = input("Do you want to play the number guessing game again ? Y/N : ")    

main()