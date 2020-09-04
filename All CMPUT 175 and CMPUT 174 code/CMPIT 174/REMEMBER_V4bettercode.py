# Remember The Word Version 4
# This program does the following:
# create the window, display the icon and display instructions
# prompt player to press enter
# display words
# get guess
# display results - output win or condolence message but not both
# end game by closing the window
# replace adjacent duplicate line groups  with a repetition
# control structure - for statement
# limit the occurrence of literals
# MULTIPLE OCCURRENCES OF NON-ADJACENT LINE GROUPS
# USES USER DEFINED FUNCTIONS
# Main Algorithm
import time,random
from uagame import Window

def create_window():
	# this is user defined function creates the window 
	# and returns the window
	title = 'Remember The Word'
	width = 500
	height = 400
	window = Window(title,width,height)
	return window

def display_icon(window):# function definition statement
	# -window is a parameter is a uagame.Window object
	icon_color = 'green'
	icon_size = 100
	icon_string = 'UA'
	window.set_font_color(icon_color)
	window.set_font_size(icon_size)
	window_width = window.get_width()
	icon_width = window.get_string_width(icon_string)
	x_icon = window_width - icon_width
	y_icon = 0
	window.draw_string(icon_string,x_icon,y_icon)
	# return statement not required - think about the Bowen example
def display_instructions(window):
	# displays the instructions
	# - window is a uagame.Window object
	text_size = 24
	text_color = 'white'
	window.set_font_size(text_size)
	window.set_font_color(text_color)
	x = 0
	y = 0
	font_height = window.get_font_height()
	# create instruction list
	instruction_list = ['A sequence of words will be displayed','You will be asked which words starts with','a particular letter.','You win if you enter the right word.']
	
	# Use for statement to display the instructions
	for instruction in instruction_list:
		window.draw_string(instruction,x,y)
		y = y + font_height
	# prompt player to press enter
	prompt1 = 'Press the enter key to display the words.'
	window.input_string(prompt1,x,y)
def display_words(window,word_list): # function definition with 2 parameters
	# displays the words in the word_list
	# - window is the uagame.Window object
	# - word_list is a list of words
	text_color = 'white'
	text_size = 24
	x = 0
	y = 0
	pause_time = 2
	
	# Use for statement to display the word
	for word in word_list:
		window.set_font_size(text_size)
		window.set_font_color(text_color)		
		window.draw_string(word,x,y)
		time.sleep(pause_time)
		# CLEAR WINDOW
		window.clear()
		# DISPLAY ICON
		display_icon(window) # 2nd funciton call
	# does not need a return statement
def get_guess(window,start_letter):
	# asks the user to enter a word and returns the guess
	# - window is uagame.Window object
	# - start_letter is the first letter of the correct_answer
	text_size = 24
	text_color = 'white'
	x = 0
	y = 0
	window.set_font_size(text_size)
	window.set_font_color(text_color)
	prompt_for_word = 'What word starts with the letter '+start_letter+'?'
	guess = window.input_string(prompt_for_word,x,y)
	return guess 
def display_results(window,correct_answer,guess):
	# displays the results
	# -window is uagame.Window object
	# - correct_answer is the word to be guess
	# - guess is the player input
	text_size =24
	text_color = 'white'
	window.set_font_size(text_size)
	window.set_font_color(text_color)
	font_height = window.get_font_height()
	x = 0
	y = 0
	win_message = 'Congratulations, you are correct.'
	lose_message = 'Sorry you entered ' + guess
	correct_answer_message = 'The correct answer was '+correct_answer
	if guess == correct_answer:
		window.draw_string(win_message,x,y)
	else:
		window.draw_string(lose_message,x,y)
	y = y + font_height
	window.draw_string(correct_answer_message,x,y)
	# return is not required
def end_game(window):
	# ends the game
	# - window is uagmae.Window object
	font_size = 24
	window.set_font_color('white')
	window.set_font_size(font_size)
	font_height = window.get_font_height()
	x = 0
	window_height = window.get_height()
	y = window_height - font_height
	prompt2 = 'Press enter to end the game.'
	window.input_string(prompt2,x,y)
	window.close()
def main():
	# The items below are required by other functions
	word_list = ['orange','chair','mouse','sandwich']
	correct_answer = random.choice(word_list)
	start_letter = correct_answer[0]	
	# create window
	window = create_window() # function call to create_window

	# display icon
	display_icon(window) # function call - window is the argument 
	
	# display instructions
	display_instructions(window) # function call window is the argument

	# CLEAR WINDOW
	window.clear()
	# DISPLAY ICON
	display_icon(window) # function call window is the argument
	
	# display words
	display_words(window,word_list) # function call with 2 arguments
	
	# get guess
	guess = get_guess(window,start_letter) #function call
	# CLEAR WINDOW
	window.clear()
	# DISPLAY ICON
	display_icon(window) # 3rd function call
	# display results
	display_results(window,correct_answer,guess)
	# end game
	end_game(window)
main()
