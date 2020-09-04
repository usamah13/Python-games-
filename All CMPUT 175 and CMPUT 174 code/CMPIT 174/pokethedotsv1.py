# Poke the Dots - Version 1
#
# Poke the dots is a game where two dots move around
# in a window, bouncing off sides. If the two dots ever
# collide, then the game is over. The player earns 1
# point per second before the dots have collided.
# Player can tap the screen to move dots to new,
# random locations.
#
# Version 1 implements the following features:
#   - In this version, dots wrap around the screen
#     rather than bounce off sides
#   - Collisions are not detected
#   - This version does not implement clicking to
#     randomly replace dots
#   - Version 1 does not implement points
from uagame import Window
import time
import pygame
from pygame.locals import *
import random


# User-defined functions

def main():
    window = Window('Poke the Dots', 500, 400)
    window.set_auto_update(False)
    game = Game(window)
    game.play()
    window.close()

# User-defined classes
class Game:
    # An object in this class represents a complete game.

    def __init__(self, window):
        # Initialize a Game.
        # - self is the Game to initialize
        # - window is the uagame window object
        
        self.window = window
        self.bg_color = pygame.Color('black')
        self.pause_time = 0.04 # smaller is faster game
        self.close_clicked = False
        self.continue_game = True
        
        # initialize dots; choose starting location randomly
        small_center = [random.randint(0, 500), random.randint(0,400)]
        large_center = [random.randint(0, 500), random.randint(0,400)]        
        self.small_dot = Dot(pygame.Color("red"), 30, small_center, [2, 1], self.window.get_surface())
        self.large_dot = Dot(pygame.Color("blue"), 40, large_center, [1, 2], self.window.get_surface())
    
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
        self.small_dot.draw()
        self.large_dot.draw()
        self.window.update()        
        
    def update(self):
        # Update the game objects.
        # - self is the Game to update
        
        # we need to update the position of our dots
        self.small_dot.update()
        self.large_dot.update()
             
    def decide_continue(self):
        # Check and remember if the game should continue
        # - self is the Game to check
        
        # check if there is a 'close window' event
        pass

class Dot:
    def __init__(self, color, radius, center, velocity, surface):
        # this method initializes our a dot object
        #   - self   : the object that we are initializing
        #   - color : the color the dot is drawn in; must be a pygame Color object
        #   - radius: the distance between the center of the circle and its edge; must be integer
        #   - center: the middle point of the dot; must be in list form [x, y]
        #   - velocity: speed and direction of the dot; must be in list form [x, y]  where negative values mean up/left and positive values mean down/right
        #   - surface: the surface on which we draw the dot
        self.color   = color
        self.radius = radius
        self.center = center
        self.velocity = velocity
        self.surface = surface
                
    def draw(self):
        # draws a dot on its specified surface
        #   - self : the Dot object that is being drawn
        pygame.draw.circle(self.surface, self.color, self.center, self.radius)
    
    def update(self):
        # move the dot to a new position, based on its velocity. For Version 1,
        # If the dot reaches the edge of the screen, it wraps to the other side.
        #   - self: the Dot object to be moved
        window_width = 500
        window_height = 400
        
        # update our x-coordinate and and wrap along x-axis
        self.center[0] = (self.center[0] + self.velocity[0]) % window_width
        # update our y-coordinate and wrap along y-axis
        self.center[1] = (self.center[1] + self.velocity[1]) % window_height

    
main()
