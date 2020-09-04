# Word Puzzle Version 1 
# This is a game in which the user is prompted to enter the miising letter of a
# random word
# The game then provides feedback according to the user guess. 


import random
import uagame

def main():

    # create window
    screen_width = 600
    screen_height = 600
    window = uagame.Window('Word Puzzle', screen_width, screen_height)
    # display instructions 
    window.set_font_size(24)
    window.set_font_color('white')
    instructions = ['I am tinking of a secerct word.',
                    'Try and guess the word. You can guess one letter',
                    'at a time. Each time you guess I will show you',
                    'which letters have been coreectly guessed and which',
                    'letters are still missing. You will have 4 guesses to',
                    'guess all the letter. Good luck!']
                    
    x = 0
    y = 0
    for line in instructions:
            window.draw_string(line, x, y)
            font_height = window.get_font_height()
            y = y + font_height            
               
    
    
    # create a list of words to be used 
    Words_list = ['apple','banana','watermelon','kiwi','pineapple','mango']
    word = random.choice(Words_list)
    # alternative way is to use random.randint(1, (len(Words_liost)-1)
    selected_word= word[1:]
    window.draw_string('The answer so far is _'+ selected_word, x, y)
    
    # prompt user to guess the letter
    
    y = y + font_height
    guess = window.input_string('Guess a letter: ',x, y)
    
    # Provide Feedback
    # can also use guess == word[:1]
    if guess == word[0]:
        
        y = y + font_height
        window.draw_string('Good Job! You found the word '+ word+'!',x, y)
    else:
        
        y = y + font_height
        window.draw_string('Not quite, the correct word was '+ word+'. Better luck next time',x, y)
    
    # prompt user to exit program
    y = y + font_height
    window.input_string('Press enter to end the game.',x,y)
    window.close()
      
main()
