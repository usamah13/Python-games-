# Remember The Word Version 2
# This program does the following:
# create the window, display the icon and display instructions
# prompt player to press enter
# display words
# get guess
# display results - output win or condolence message but not both
# end game by closing the window

# Main Algorithm
import time
from uagame import Window
def main():
	# create window
	window = Window('Remember The Word',500,400)

	# display icon
	window.set_font_color('green')
	window.set_font_size(100)
	window_width = window.get_width()
	icon_width = window.get_string_width('UA')
	x_icon = window_width - icon_width
	y_icon = 0
	window.draw_string('UA',x_icon,y_icon)
	
	# display instructions
	window.set_font_size(24)
	window.set_font_color('white')
	x = 0
	y = 0
	window.draw_string('A sequence of words will be displayed.',x,y)
	font_height = window.get_font_height()
	y = y + font_height
	window.draw_string('You will be asked which word starts with',x,y)
	y = y+font_height
	window.draw_string('a particular letter.',x,y)
	y = y + font_height
	window.draw_string('You win if you enter the right word.',x,y)
	y = y+font_height
	# prompt player to press enter
	window.input_string('Press the enter key to display the words.',x,y)

	# CLEAR WINDOW
	window.clear()
	# DISPLAY ICON
	window.set_font_size(100)
	window.set_font_color('green')
	window.draw_string('UA',x_icon,y_icon)
	
	# display words
	# display word 1
	window.set_font_size(24)
	window.set_font_color('white')
	x = 0
	y = 0
	window.draw_string('orange',x,y)
	time.sleep(2)
	# CLEAR WINDOW
	window.clear()
	# DISPLAY ICON
	window.set_font_size(100)
	window.set_font_color('green')
	window.draw_string('UA',x_icon,y_icon)	
	
	# display word 2
	window.set_font_size(24)
	window.set_font_color('white')	
	window.draw_string('chair',x,y)
	time.sleep(2)
	# CLEAR WINDOW
	window.clear()
	# DISPLAY ICON
	window.set_font_size(100)
	window.set_font_color('green')
	window.draw_string('UA',x_icon,y_icon)	
	
	# display word 3
	window.set_font_size(24)
	window.set_font_color('white')	
	window.draw_string('mouse',x,y)
	time.sleep(2)
	# COPY AND PASTE HERE
	# CLEAR WINDOW
	window.clear()
	# DISPLAY ICON
	window.set_font_size(100)
	window.set_font_color('green')
	window.draw_string('UA',x_icon,y_icon)
	
	# display word 4
	window.set_font_size(24)
	window.set_font_color('white')	
	window.draw_string('sandwich',x,y)
	time.sleep(2)

	# CLEAR WINDOW
	window.clear()
	# DISPLAY ICON
	window.set_font_size(100)
	window.set_font_color('green')
	window.draw_string('UA',x_icon,y_icon)	

	# get guess
	window.set_font_size(24)
	window.set_font_color('white')
	guess = window.input_string('What word starts with the letter c?',x,y)
	# CLEAR WINDOW
	window.clear()
	# DISPLAY ICON
	window.set_font_size(100)
	window.set_font_color('green')
	window.draw_string('UA',x_icon,y_icon)
	# display results
	window.set_font_size(24)
	window.set_font_color('white')
	if guess == 'chair':
		window.draw_string('Congratulations, you are correct.',x,y)
	else:
		window.draw_string('Sorry you entered '+guess,x,y)
	y = y + font_height
	window.draw_string('The correct answer was chair.',x,y)
	# end game
	x = 0
	window_height = window.get_height()
	y = window_height - font_height
	window.input_string('Press enter to end the game.',x,y)
	window.close()
main()
