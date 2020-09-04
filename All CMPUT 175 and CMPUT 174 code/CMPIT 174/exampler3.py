# Exemplar Graphics-3
# This is an example program that contains graphics, using
# modules uagame.
# It contains these kinds of statements: expression, assignment,
# import, function definition, while, return
# It contains these kinds of expressions: identifier, literal,
# attribute reference, function call, binary operator, expression
# list
# It uses these types:
# str, int, float, bool, NoneType, function, module, 
# uagame.Window

import time
import uagame

def main():
    window = create_window()
    count = play(window)
    end_game(window, count)
   
def create_window():
    # Create a Window object and return it
    title = 'Graphics Example 3'
    width = 500
    height = 400
    window = uagame.Window(title, width, height)
    window.set_auto_update(False)
    return window

def play(window):
    # Play the game repeatedly until the play wishes to quit.
    # Return the number of times the game was played
    # - window is the uagame.Window object to display prompt

    play_again = True
    play_count = 0
    while play_again:
        play_count = play_count + 1
        play_round(window)
        play_again = should_continue(window)
    return play_count
    
def play_round(window):
    # Play one round of the game.
    # - window is the uagame.Window object to display prompt
    x_string = 'x'
    y_string = 'y'
    word = pick_word(window)
    color = pick_color(window)
    x = pick_coord(window, x_string)
    y = pick_coord(window, y_string)
    old_font_color = window.get_font_color()
    window.set_font_color(color)
    window.draw_string(word, x, y)
    window.update()
    window.set_font_color(old_font_color)
    
def pick_word(window):
    # Return a string typed by the player
    # - window is the uagame.Window object to display prompt

    word_prompt = 'Please type a word and press enter >'
    word = window.input_string(word_prompt, 0,0)
    window.clear()
    return word

def pick_color(window):
    # Returnthe colour word typed in by the player
    # - window is the uagame.Window object to display prompt    
    color_prompt = 'Please type a color and press enter >'
    color = window.input_string(color_prompt, 0,0)
    window.clear()
    return color

def pick_coord(window, coord):
    # Return an int that represents a coordinate selected by the
    # player
    # - window is the uagame.Window object to display prompt    
    # - coord is the string name of the coord to prompt for
    
    prompt_prefix = 'Please type a(n) '
    prompt_suffix = ' coord in window and press enter >'
    coord_string = window.input_string(prompt_prefix + coord + prompt_suffix, 0,0)
    coord = int(coord_string)
    window.clear()
    return coord 

def should_continue(window ):
    # Return True if the player wants to play again.
    # Otherwise return False
    # - window is the uagame.Window object to display prompt    
    
    play_prompt = 'Do you want to play again (yes or no)?'
    answer = window.input_string(play_prompt, 0,0)
    window.clear()
    return answer == 'yes'
    
def end_game(window, count):
    # End the game by reporting the number of times it was
    # played.
    # - window is the uagame.Window object to display prompt        
    # - count is the int number of times the game was played

    thanks = 'Thanks for playing ' + str(count) + ' time(s).'
    window.clear()
    window.draw_string(thanks, 0,0)
    window.update()
    time.sleep(2)
    window.close()
main()
