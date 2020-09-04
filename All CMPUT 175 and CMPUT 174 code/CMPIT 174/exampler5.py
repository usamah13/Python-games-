# Exemplar Graphics-5
# This is an example program that contains graphics using
# the pygame module, contains user-defined classes, and 
# responds to multiple kinds of events.
# It contains these kinds of statements: expression, assignment,
# import, function definition, while, for, if, return, class
# definition
# It contains these kinds of expressions: identifier, literal,
# attribute reference, function call, binary operator, expression
# list
# It uses these types: str, int, float, bool, NoneType, function,
# module, tuple, pygame.Color, pygame.Rect, Game,
# Circle

from uagame import Window
import pygame, time
from pygame.locals import *

# User-defined functions

def main():

   window = Window('Exemplar Graphics 5', 500, 400)
   window.set_auto_update(False)
   game = Game(window)
   game.play()
   window.close()

# User-defined classes

class Circle:
   # An object in this class represents a colored circle.

   def __init__(self, center, radius, color, window):
      # Initialize a Cirlcle.
      # - self is the Circle to initialize
      # - center is a list containing the x and y int
      # coords of the center of the Circle
      # - radius is the int pixel radius of the Circle
      # - color is the pygame.Color of the Circle
      # - window is the uagame window object

      self.center = center
      self.radius = radius
      self.color = color
      self.window = window
   
   def draw(self):
      # Draw the Circle.
      # - self is the Circle to draw
      
      pygame.draw.circle(self.window.get_surface(), self.color, self.center, self.radius)
   
   def move(self):
      # Move the circle.
      # - self is the Circle to move
      
      window_size = (self.window.get_width(), self.window.get_height())
      for index in range(0, 2):
         self.center[index] = (self.center[index] + 1) % window_size[index]
         
   def get_color(self):
      # Return the color of the Circle.
      # - self is the Circle
      
      return self.color
   
   def enlarge(self, increment):
      # Enlarge the radius of the Circle.
      # - self is the Circle
      # - increment is the int number of pixels
      # to add to the radius
      
      self.radius = self.radius + increment

class Game:
   # An object in this class represents a complete game.

   def __init__(self, window):
      # Initialize a Game.
      # - self is the Game to initialize
      # - window is the uagame window object
      
      self.window = window
      self.bg_color = pygame.Color('black')
      self.fg_color_str = "green"
      self.pause_time = 0.04 # smaller is faster game
      self.close_clicked = False
      self.continue_game = True
      self.circle = Circle([200, 200], 20, pygame.Color(self.fg_color_str), window)
      self.elapsed_time = 0
      self.end_time = 5
      self.radius_increment = 5

   def play(self):
      # Play the game until the player presses the close box.
      # - self is the Game that should be continued or not.

      while not self.close_clicked:  # until player clicks close box
          # play frame
          self.handle_event()
          self.draw()            
          if self.continue_game:
              self.update()
              self.decide_continue()
          time.sleep(self.pause_time) # set game velocity by pausing

   def handle_event(self):
      # Handle each user event by changing the game state
      # appropriately.
      # - self is the Game whose events will be handled

      event = pygame.event.poll()
      if event.type == QUIT:
         self.close_clicked = True
      elif event.type == MOUSEBUTTONUP and self.continue_game:
         self.handle_mouse_up()

   def handle_mouse_up(self):
      # Respond to the player releasing the mouse button by
      # taking appropriate actions.
      # - self is the Game where the mouse up occurred

      self.circle.enlarge(self.radius_increment)

   def draw(self):
      # Draw all game objects.
      # - self is the Game to draw
      
      self.window.clear()
      self.circle.draw()
      if not self.continue_game:
         # Perform appropriate game over actions
         self.window.set_bg_color(self.fg_color_str)
         self.window.clear()
      self.window.update()

   def update(self):
      # Update the game objects.
      # - self is the Game to update
      
      self.circle.move()
      self.elapsed_time = pygame.time.get_ticks() // 1000
         
   def decide_continue(self):
      # Check and remember if the game should continue
      # - self is the Game to check
      
      if self.elapsed_time > self.end_time:
         self.continue_game = False

main()
