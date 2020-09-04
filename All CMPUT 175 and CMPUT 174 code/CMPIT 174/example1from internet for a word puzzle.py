from random import choice

# Removed WORD variable since you don't really need it
word = choice(('apple', 'oracle',
                     'amazon', 'microsoft'))

# Removed correct variable since it points to word and is therefore not
# needed

clue = word[0] + word[::-1][0]    # Simplified slices
# Removed redundant letter_guess = '', since 
# this is overwritten in the while loop
word_guess = ''
store_letter = ''
count = 0
limit = 5

print('Welcome to "Guess the Word Game!"')
print('You have 5 attempts at guessing letters in a word')
print("Let's begin!")
print('\n')    # print('\n') prints a newline,
                  # not a blank line, maybe use
                  # print()

while count < limit:
    letter_guess = input('Guess a letter: ')
    count += 1
    # Moved count += 1 here so count doesn't have
    # to be incremented twice

    if letter_guess in word:
        print('yes!')
        store_letter += letter_guess

    else:
    # if letter_guess not in word:
        print('no!')

    if count == 2:
        print('\n')
        clue_request = input('Would you like a clue? [y / n] ')
        # Added "[y / n]" to make it clear the 
        # user can only use those responses
        if clue_request == 'y':
            print('\n')
            print('CLUE: The first and last letter of the word is: ', clue)
        elif clue_request == 'n':
            # Changed to elif
            print("You're very brave!")

print('\n')
print('Now its time to guess. You have guessed '+ str(len(store_letter))+ ' letter(s) correctly')

print('These letters are: ', store_letter)

word_guess = input('Guess the whole word: ')

# Removed useless while loop (both if and else 
# statements break out of the loop)

if word_guess.lower() == word:
    print('Congrats!')
else:
    # You don't have to write out a whole
    # elif condition, just use else-
    print('Unlucky! The answer was,', word)


print('\n')
input('Press Enter to leave the program ')
# This last input may be redundant if your only
# option is to leave