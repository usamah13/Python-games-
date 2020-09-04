# Remember the word Version 4
#
# Displays 4 words to users. User is prompted to recall one of
# those four words. This is the the first programming project
# in CMPUT174, Winter 2018.
#
# We are now using loops to replace adjacent duplicate line
# groups for displaying instructions and words to guess.
# We have also replaced repeating literals with variables.
import time, random, uagame

def main():
    # Create window
    window_width = 500
    window_height = 400
    window = uagame.Window('Remember The Word', window_width, window_height)
    
    # display logo    
    draw_logo(window)
    
    # display instructions
    text_size = 24
    text_color = 'white'
    draw_instructions(window, text_size, text_color) 
        
    # present words: orange, chair, mouse, sandwich
    # sample correct answer from choices; randomize presentation order
    word_names = [ 'chair', 'orange', 'mouse', 'sandwich' ]
    correct_answer = random.choice(word_names)
    random.shuffle(word_names)
    draw_words(window, text_size, text_color, word_names)
       
    # prompt user for input
    guess = get_guess(window, text_size, text_color, correct_answer[0])

    # display feedback
    draw_feedback(window, text_size, text_color, guess, correct_answer)
 
    # terminate program
    window.close()
     
def draw_feedback(window, text_size, text_color, guess, correct_answer, text_x=0, text_y=0):
    # Tells user if their answer was correct or incorrect.
    #  - window   : the window to display feedback to
    #  - text_size : the size of text for displaying feedback
    #  - text_color: the color of text for displaying feedback
    #  - guess      : the user's input; we are checking if it is correct or incorrect
    #  - correct_answer : the correct answer the user is trying to guess
    #  - text_x     : the x-position for drawing feedback
    #  - text_y     : the y-position for drawing feedback
    window.clear()
    draw_logo(window)
    window.set_font_size(text_size)
    window.set_font_color(text_color)    

    if guess == correct_answer:
        window.draw_string('Congratulations, you are correct.', text_x, text_y)
    else:
        window.draw_string('Sorry, you entered ' + guess, text_x, text_y)
        
    text_y = text_y + window.get_font_height()
    window.draw_string('The answer was ' + correct_answer, text_x, text_y)
        
    text_y = window.get_height() - window.get_font_height()
    window.input_string('Press enter to end the game.', text_x, text_y)    
    
def get_guess(window, text_size, text_color, first_letter, text_x=0, text_y=0): 
    # Prompts the user to provide a guess about the correct answer.
    #  - window   : the window to display the prompt on
    #  - text_size : the size of text for displaying the prompt
    #  - text_color: the color of text for displaying the prompt
    #  - first_letter: the first letter of the correct answer; supplied in prompt
    #  - text_x     : the x-position for drawing the prompt
    #  - text_y     : the y-position for drawing the prompt    
    window.clear()
    draw_logo(window)
    window.set_font_size(text_size)
    window.set_font_color(text_color)    
    guess = window.input_string('What word begins with the letter ' + first_letter + '?', text_x, text_y)
    return guess
 
def draw_words(window, text_size, text_color, word_names, text_x=0, text_y=0):
    # Draws a list of words on screen, one at a time, separated by an interval.
    # Screen is cleared before each new word is displayed.
    #  - window   : the window to display the words on
    #  - text_size : the size of text for displaying words
    #  - text_color: the color of text for displaying words
    #  - word_names: a list of words to display
    #  - text_x     : the x-position for drawing the words
    #  - text_y     : the y-position for drawing the words   
    sleep_time = 2
    for word in word_names:
        # clear screen
        window.clear()
        
        # display word
        window.set_font_size(text_size)
        window.set_font_color(text_color)           
        window.draw_string(word, text_x, text_y)
        
        # display logo
        draw_logo(window)
        
        # waits appropriate amount of time between displaying words
        time.sleep(sleep_time)    
 
def draw_instructions(window, text_size, text_color, text_x=0, text_y=0):
    # Presents user with instructions for the game.
    #  - window   : the window to display the instructions on
    #  - text_size : the size of text for displaying instructions
    #  - text_color: the color of text for displaying instructions
    #  - text_x     : the x-position for drawing the instructions
    #  - text_y     : the y-position for drawing the instructions
    window.set_font_size(text_size)
    window.set_font_color(text_color)    
    instructions = [ 'A sequence of words will be displayed.',
                     'You will be asked which word starts with',
                     'a particular letter.', 
                     'You win if you enter the right word.']

    for line in instructions:
        window.draw_string(line, text_x, text_y)
        text_y = text_y + window.get_font_height()    

    # Wait for user before moving on to next step
    window.input_string('Press enter key to display the words.', text_x, text_y)
 
def draw_logo(window):
    # Presents the UofA logo in the top-right corner of the screen
    #  - window   : the window to display the logo on
    logo_string = 'UA'
    logo_size = 105
    logo_color = 'green'
    x_logo = window.get_width() - window.get_string_width(logo_string)
    y_logo = 0
    window.set_font_size(logo_size)
    window.set_font_color(logo_color)
    window.draw_string(logo_string, x_logo, y_logo)

main()
