# Pong Version 3
# In this game two users play ping pong by moving paddles
# vertically near the two screen edges.
# In this version the scores are recorded and the ball bounces from the screen and front of the paddle
# and 2 players play the game using the keyboard

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
        pygame.key.set_repeat(20, 20)
        # initialize ball and paddles(rectangles); choose starting location randomly
        surface = window.get_surface()
        self.window_size = self.window.get_surface().get_size()
        ballcolor = pygame.Color('white')
        center = [250,200] # The center of the window
        radius = 3
        velocity = [2,1]
        rectx = 100
        recty = 175
        rectwidth = 20
        rectheight = 100
        self.ball = Ball(surface,ballcolor,center,radius,velocity)
        self.rect_left = pygame.Rect(rectx, recty, rectwidth, rectheight)
        self.rect_right = pygame.Rect((self.window_size[0] - rectx), recty, rectwidth, rectheight)
        
        self.rectcolor = pygame.Color('white')
        self.score = [0,0]
        self.max_score = [11,11]
        
       
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
        elif event.type == KEYDOWN and self.continue_game:
            self.handle_keydown(event)
    
    def handle_keydown(self, event):
        window_size = self.window.get_surface().get_size()
        list_of_keys = pygame.key.get_pressed()
        
        # right paddle
        if list_of_keys[K_p] == True and self.rect_right.top != 0: 
            self.rect_right= self.rect_right.move(0, -5)
        if list_of_keys[K_l] == True and self.rect_right.bottom != window_size[1]: 
                        self.rect_right= self.rect_right.move(0, 5)
        #left paadle
        if list_of_keys[K_q] == True and self.rect_left.top != 0: 
                        self.rect_left= self.rect_left.move(0, -5)
        if list_of_keys[K_a] == True and self.rect_left.bottom != window_size[1]: 
                        self.rect_left= self.rect_left.move(0, 5)        
            
   
    def draw(self):
           # Draw all game objects.
           # - self is the Game to draw       
        self.window.clear()
        self.ball.draw()
        surface = self.window.get_surface()
        pygame.draw.rect(surface, self.rectcolor, self.rect_left)
        pygame.draw.rect(surface, self.rectcolor, self.rect_right)
        self.draw_score()
        self.window.update()        
           
    def update(self):
           # Update the game objects.
           # - self is the Game to update
           
           # we need to update the position of our dots
        #print(type(self.ball)) # to get type
        self.ball.update()
        
        for i in range(len(self.ball.center)):
            if self.rect_left.collidepoint(self.ball.center):
                if self.ball.velocity[0] > 0:
                    self.ball.velocity[0]*=1
                else:
                    self.ball.velocity [0]*= -1
                
                
            if self.rect_right.collidepoint(self.ball.center):
                if self.ball.velocity[0] < 0:
                    self.ball.velocity[0]*=1
                else:
                    self.ball.velocity [0]*= -1     
        if self.ball.center[0] - self.ball.radius < 0 :
            self.score[1] += 1
        if self.ball.center[0] + self.ball.radius > self.window_size[0]:
            self.score[0] += 1
        
        
                
    def decide_continue(self):
           # Check and remember if the game should continue
           # - self is the Game to check
           
           # check if there is a 'close window' event
        if self.score[0] == self.max_score[0] or self.score[1] == self.max_score[1]:
            self.continue_game = False
        
    def draw_score(self):
            # Draw the time since the game began as a score
            # in white on the window's background.
            # - self is the Game to draw for.
            score_left = str(self.score[0])
            score_right = str(self.score[1])
            self.window.set_font_color('white')
            self.window.set_font_size(48)
            x = 0 
            y = 0
            window_width  = 500
            xright = window_width - self.window.get_string_width(score_right)
            self.window.draw_string(score_left, x, y)
            self.window.draw_string(score_right, xright, y) 
            
   
class Ball:
    def __init__(self,surface,color,center,radius,velocity):
    # this method initializes our a Ball object
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
        size = self.surface.get_size()
        
        for i in range(len(self.center)):
            self.center[i] =(self.center[i] + self.velocity[i]) 
            if self.center[i] - self.radius < 0 or self.center[i] + self.radius > size[i]:
                self.velocity[i] *= -1
                
            
        # update our x-coordinate and and wrap along x-axis
        #self.center[0] = (self.center[0] + self.velocity[0]) % size[0]
        # update our y-coordinate and wrap along y-axis
        #self.center[1] = (self.center[1] + self.velocity[1]) % size[1]
   
main()    