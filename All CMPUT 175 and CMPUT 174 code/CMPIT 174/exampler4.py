# Exemplar Graphics-4
# This is an example program that contains graphics, using
# modules pygame and uaio and responds to a close window event.
# It contains these kinds of statements: expression, assignment,
# import, function definition, while, return, class definition
# It contains these kinds of expressions: identifier, literal,
# attribute reference, function call, binary operator, expression
# list
# It uses these types:
# str, int, float, bool, NoneType, function, module, tuple
# , pygame.Rect, Game


from uagame import Window
import time
import pygame
from pygame.locals import *

# User-defined functions

def main():

    window = Window('Exemplar Graphics 4', 500, 400)
    window.set_auto_update(False)
    game = Game(window)
    game.play()
    window.close()

# User-defined classes

class Game:
    # An object in this class represents a complete game.
    # Any Game class can use the following six methods 

    def __init__(self, window):
        # Initialize a Game.
        # - self is the Game to initialize
        # - window is the uagame window object
        # Any Game class can use the following four attributes
        self.window = window
        self.bg_color = pygame.Color('black')
        self.pause_time = 0.04 # smaller is faster game
        self.close_clicked = False
        self.continue_game = True
        self.rectangle = pygame.Rect(100, 200, 50, 25)
        self.rect_color = pygame.Color('green')
    
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
        # - self is the Game whose events will be handled.

        event = pygame.event.poll()
        if event.type == QUIT:
            self.close_clicked = True

    def draw(self):
        # Draw all game objects.
        # - self is the Game to draw
        
        self.window.clear()
        pygame.draw.rect(self.window.get_surface(), self.rect_color, self.rectangle)
        self.window.update()

    def update(self):
        # Update the game objects.
        # - self is the Game to update
        coord_increment = 2
        self.rectangle.move_ip(coord_increment, coord_increment)
             
    def decide_continue(self):
        # Check and remember if the game should continue
        # - self is the Game to check
        # write code to check if we should continue the game
        pass
    
main()
