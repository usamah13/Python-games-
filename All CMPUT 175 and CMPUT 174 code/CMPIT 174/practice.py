# Fox Bunny Chase
# In this game, the user tries to prevent two moving animals
# from colliding by pressing and releasing the mouse
# to teleport the fox to the top left corner of the window
# and the bunny to a random location.
# The score is the number of seconds from start of game
# until the two animals collide.

import pygame, random, time, math
from uagame import Window
from pygame.locals import *

# User-defined functions

def main():

	window = Window('Fox Bunny Chase', 500, 400)
	window.set_auto_update(False)
	game = Game(window)
	game.play()
	window.close()

# User-defined classes

class Game:
	
	def __init__(self, window):
    	# Initialize a Game.
    	# - self is the Game to initialize
    	# - window is the uagame window object
		self.window = window
		self.bg_color = 'black'
		self.pause_time = 0.01 # smaller is faster game
		self.close_clicked = False
		self.continue_game = True
		self.bunny_color = 'grey'
		self.fox_color = 'brown'
		self.bunny = Animal(self.bunny_color, [50,75], 30, [1,3], window.get_surface())
		self.fox = Animal(self.fox_color, [200,100], 40, [3,1], window.get_surface())
		self.score = 0
		self.bunny.reset()
		self.fox.randomize()
	def play(self):
    	# Play the game until the player presses the close box.
    	# - self is the Game that should be continued or not.

		while not self.close_clicked:
			# play frame
			self.handle_event()
			self.draw()
			if self.continue_game:
				self.update()
				self.decide_continue() # should game continue?
				time.sleep(self.pause_time) # set game velocity by pausing

	def handle_event(self):
    	# Handle one user event by changing the game state
    	# appropriately.
    	# - self is the Game whose events will be handled.

		event = pygame.event.poll()
		if event.type == QUIT:
			self.close_clicked = True
		elif event.type == MOUSEBUTTONUP and self.continue_game:
			self.handle_mouse_up(event)

	def handle_mouse_up(self, event):
    	# Respond to the player releasing the mouse button by
    	# taking appropriate actions.
    	# - self is the Game where the mouse up occurred.
    	# - event is the pygame.event.Event object to handle

		self.bunny.randomize()
		self.fox.reset()

	def draw(self):
    	# Draw all game objects.
    	# - self is the Game to draw

		self.window.clear()
		self.bunny.draw()
		self.fox.draw()
		self.draw_score()
		if not self.continue_game:  # Perform game over actions
			self.draw_game_over()
		self.window.update()

	def update(self):
    	# Update all game objects with state changes
    	# that are not due to user events
    	# - self is the Game to update
	
		self.bunny.move()
		self.fox.move()
		self.score = pygame.time.get_ticks() // 1000

	def decide_continue(self):
    	# Determine if the game should continue
    	# - self is the Game to update

		if self.bunny.intersects(self.fox):
			self.continue_game = False

	def draw_game_over(self):
    	# Draw BUNNY CAUGHT in the lower left corner of the
    	# window, using the bunny’s color for the font
    	# and the fox's color as the background
    	# - self is the Game to draw for.

		game_over_string = 'BUNNY CAUGHT'
		self.window.set_font_color(self.bunny_color)
		self.window.set_bg_color(self.fox_color)
		self.window.set_font_size(64)
		height = self.window.get_height() - self.window.get_font_height()
		self.window.draw_string(game_over_string, 0, height)
		self.window.set_bg_color(self.bg_color)

	def draw_score(self):
    	# Draw the time since the game began as a score
    	# in white on the window's background.
    	# - self is the Game to draw for.

		string = 'Score: ' + str(self.score)
		self.window.set_font_color('white')
		self.window.set_font_size(72)
		self.window.draw_string(string, 0, 0)

class Animal:
	# An object in this class represents a colored circle
	# that can move.

	def __init__(self, color, center, radius, velocity, surface):
    	# Initialize a Dot.
    	# - self is the Animal to initialize
    	# - color is the pygame.Color of the animal
    	# - center is a list containing the x and y int
    	# coords of the center of the animal
    	# - radius is the int pixel radius of the animal
    	# - velocity is a list containing the x and y components
    	# - surface is the window's pygame.Surface object

		self.color = pygame.Color(color)
	
		self.center = center
		self.radius = radius
		self.velocity = velocity
		self.surface = surface

	def draw(self):
    	# Draw the animal on the surface
    	# - self is the animal

		pygame.draw.circle(self.surface, self.color, self.center, self.radius)

	def move(self):
    	# Change the location and the velocity of the Animal so it
    	# remains on the surface by bouncing from its edges.
    	# - self is the animal

		size = self.surface.get_size()
		for coord in range(0, 2):
			self.center[coord] = self.center[coord] + self.velocity[coord]
			# check top, bottom, left and right edges
			if (self.center[coord] < self.radius) or (self.center[coord] + self.radius > size[coord]):
				self.velocity[coord] = - self.velocity[coord]

	def intersects(self, animal):
	# Return True if the two animals intersect and False if
	# they do not.
	# - self is an Animal
	# - animal is the other Animal

		distance = math.sqrt((self.center[0] - animal.center[0])**2+(self.center[1] - animal.center[1])**2)
		return distance <= self.radius + animal.radius
	
	def reset(self):
		size = self.surface.get_size()
		for coord in range(0, 2):
			self.center[coord] = self.radius
	
	def randomize(self):
		size = self.surface.get_size()
		for coord in range(0, 2):
			self.center[coord] = random.randint(self.radius, size[coord] - self.radius)

main()


    