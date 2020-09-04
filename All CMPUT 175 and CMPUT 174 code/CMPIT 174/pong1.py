# Pong Version 1
# In this game two users play ping pong by moving paddles
# vertically near the two screen edges.
# In this version the scores are not recorded and the ball wrap around the 
# screen rather than bounce off sides.

from uagame import Window
import time
import pygame
from pygame.locals import *
import random

def main():
    #create window
    title = 'Pong'
    width = 500
    height = 400
    window = Window(title,width,height)    
    # The following statement needs to be included as we are doing 
    # window update in the code instead of having uagame do the update
    window.set_auto_update(False)
    # create Game object using window as argument
    game = Game(window)
    # Play the Game object
    game.play()
    # Close the window
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
        self.pause_time = 0.01 # smaller is faster game
        self.close_clicked = False
        self.continue_game = True
           
        # initialize ball and paddles(rectangles); choose starting location randomly
        surface = self.window.get_surface()
        windowsize = self.window.get_surface().get_size()
        ballcolor = pygame.Color('white')
        center = [250,200] # The center of the window
        radius = 3
        velocity = [1,2]
        rectx = 100
        recty = 175
        rectwidth = 10
        rectheight = 50
        self.ball = Ball(surface,ballcolor,center,radius,velocity)
        self.rect_left = pygame.Rect(rectx, recty, rectwidth, rectheight)
        self.rect_right = pygame.Rect((windowsize[0] - rectx), recty, rectwidth, rectheight)
        self.rectcolor = pygame.Color('white')
       
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
        self.ball.draw()
        surface = self.window.get_surface()
        pygame.draw.rect(surface, self.rectcolor, self.rect_left)
        pygame.draw.rect(surface, self.rectcolor, self.rect_right)
        self.window.update()        
           
    def update(self):
           # Update the game objects.
           # - self is the Game to update
           
           # we need to update the position of our dots
        #print(type(self.ball)) # to get type
        self.ball.update()
        
                
    def decide_continue(self):
           # Check and remember if the game should continue
           # - self is the Game to check
           
           # check if there is a 'close window' event
        pass
   
class Ball:
    def __init__(self,surface,ballcolor,center,radius,velocity):
    # this method initializes our a Ball object
    #   - self   : the object that we are initializing
    #   - color : the color the dot is drawn in; must be a pygame Color object
    #   - radius: the distance between the center of the circle and its edge; must be integer
    #   - center: the middle point of the dot; must be in list form [x, y]
    #   - velocity: speed and direction of the dot; must be in list form [x, y]  where negative values mean up/left and positive values mean down/right
    #   - surface: the surface on which we draw the dot
        self.color   = ballcolor
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
        size = self.surface.get_size()
        
        for i in range(len(self.center)):
            self.center[i] =(self.center[i] + self.velocity[i]) % size[i]        
        # update our x-coordinate and and wrap along x-axis
        #self.center[0] = (self.center[0] + self.velocity[0]) % size[0]
        # update our y-coordinate and wrap along y-axis
        #self.center[1] = (self.center[1] + self.velocity[1]) % size[1]
   
main()    