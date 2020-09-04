# Poke the Dots - Version 2
#
# Poke the dots is a game where two dots move around
# in a window, bouncing off sides. If the two dots ever
# collide, then the game is over. The player earns 1
# point per second before the dots have collided.
# Player can tap the screen to move dots to new,
# random locations.
#
# Version 2 implements all features EXCEPT the ability
# to click on the screeen to randomize dot locations
from uagame import Window
import time, pygame, random, math
from pygame.locals import *


# User-defined functions
def main():
    
    # Create our game window and game, then play
    # until a game end condition is met.
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
        
        # set our attribute values
        self.window = window
        self.bg_color = pygame.Color('black')
        self.pause_time = 0.02  # smaller is faster game
        self.close_clicked = False
        self.continue_game = True
        self.score = 0
        
        # our font size for displaying LARGE messages, as 
        # opposed to small messages with, e.g., more text.
        self.large_font_size = 100
        
        # initialize dots; choose starting location randomly
        window_width, window_height = self.window.get_surface().get_size()
        small_dot_radius = 30
        large_dot_radius = 40
        
        small_center = [
            random.randint(small_dot_radius, window_width-small_dot_radius),
            random.randint(small_dot_radius,window_height-small_dot_radius)
        ]
        
        large_center = [
            random.randint(large_dot_radius, window_width-large_dot_radius), 
            random.randint(large_dot_radius,window_height-large_dot_radius)
        ]         
        
        self.small_dot = Dot(pygame.Color("red"), small_dot_radius, small_center, [2,1], self.window.get_surface())
        self.large_dot = Dot(pygame.Color("blue"), large_dot_radius, large_center, [1,2], self.window.get_surface())
    
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
            time.sleep(self.pause_time)  # set game velocity by pausing
                       
    def handle_event(self):
        # Handle each user event by changing the game state
        # appropriately.
        # - self is the Game whose events will be handled.
        event = pygame.event.poll()
        if event.type == QUIT:
            self.close_clicked = True
        
    def draw_score(self):
        # Draws the scoreboard on the window in the top left corner
        #   - self: is the game to draw the score for
        self.window.set_font_size(self.large_font_size)
        self.window.set_font_color("white")
        scoreboard = "Score: " + str(int(math.floor(self.score)))
        self.window.draw_string(scoreboard, 0, 0)

    def draw_game_over(self):
        # Draws the game over message to screen if a loss condition has
        # been met
        #  - self: the game for which loss conditions are being checked
        
        # draw our game over message; red text on blue background
        # in 100pt font in the bottom-left corner of the screen
        if not self.continue_game:
            self.window.set_font_size(self.large_font_size)
            font_height = self.window.get_font_height()
            game_over_x = 0
            game_over_y = self.window.get_height() - font_height
            game_over_mssg = "GAME OVER"
                
            # we need to set the bg color back to its default value 
            # so when the screeen clears, it does not turn blue            
            orig_background_color = self.window.get_bg_color()

            self.window.set_font_color("red")
            self.window.set_bg_color("blue")            
            self.window.draw_string(game_over_mssg, game_over_x, game_over_y)
            
            self.window.set_bg_color(orig_background_color)  

    def draw(self):
        # Draw all game objects.
        # - self is the Game to draw       
        self.window.clear()
        self.small_dot.draw()
        self.large_dot.draw()
        self.draw_score()
        self.draw_game_over()        
        self.window.update()        
        
    def update(self):
        # Update the game objects.
        # - self is the Game to update
        
        # we need to update the position of our dots
        self.small_dot.update()
        self.large_dot.update()
        
        # the player gets 1 point for every second that has elapsed
        # self.score += self.pause_time
        self.score = pygame.time.get_ticks() // 1000
             
    def decide_continue(self):
        # Check and remember if the game should continue.
        # If it should not, set continue_game to False
        # - self is the Game to check
        
        # game end condition: when the two dots touch each other
        if self.small_dot.is_overlapping(self.large_dot):
            self.continue_game = False
        

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
        
        # check if the dot is moving outside of the screen on one
        # of our axes. If so, reverse its direction. Apply to all axes
        surface_boundaries = self.surface.get_size()
        for i in range(len(self.center)):
            self.center[i] += self.velocity[i]
            if self.center[i] - self.radius < 0 or self.center[i] + self.radius > surface_boundaries[i]:
                self.velocity[i] *= -1

    def is_overlapping(self, other):
        # Checks to see if we are overlapping with another dot.
        # Returns True if so, and False otherwise.
        #   - self: one dot object
        #   - other: another dot object to check for overlap with
        
        # Two dots are overlapping if their centers come within
        # a distance of the sum of their radii
        #
        # pythagorean theorem: d^2 = x^2 +y^2
        # distance is therefore: sqrt(d^2)
        #distance_x = self.center[0] - other.center[0]
        #distance_y = self.center[1] - other.center[1]
        #distance = math.sqrt(distance_x**2 + distance_y**2)
        #
        # Another way, generalizes to spaces > 2 dimensions:
        # sum the square distances along each coordinate in our  
        # positions and then take the square root of the result        
        # sumsq = 0
        # for i in range(len(self.center)):
        #     sumsq += (self.center[i] - self.other[i])**2
        # distance = math.sqrt(sumsq)
        #
        # does the same thing as the above code, but in fewer lines
        distance = math.sqrt(sum([(self.center[i] - other.center[i])**2 for i in range(len(self.center))]))
        
        return distance <= self.radius + other.radius
    

        
    
main()