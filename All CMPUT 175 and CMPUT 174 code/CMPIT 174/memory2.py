# Memory Version 2
# 
# 
import time, pygame, random
from uagame import Window
from pygame.locals import *

# User-defined functions
def main():
    # Creates the game window and game, and runs game

    window = Window('Memory', 500, 400)
    window.set_auto_update(False)
    game = Game(window)
    game.play()
    window.close()

# User-defined classes

class Game:
    # Defines a game of memory

    def __init__(self, window):
        # Initialize a Game.
        # - self is the Game to initialize
        # - window is the uagame window object
        
        # create all of the game attributes
        self.window = window
        Tile.set_window(window)
        self.pause_time = 0.04 # smaller is faster game
        self.close_clicked = False
        self.continue_game = True  
        self.score = 0
        
        self.grid = [ ]
        self.images = [ ]
        self.create_image_list()
        self.create_grid()
        
        
        
    def create_image_list(self):
        imagesname = [ ]
        for i in range(1,9):
            imgstr = 'image' +str(i)+ '.bmp'
            imagesname.append(imgstr)
            
       
        for j in range(0,8):
            img = pygame.image.load(imagesname[j])
            self.images.append(img)
            self.images.append(img)
        random.shuffle(self.images)
        
       
        
            
    def create_grid(self):
        # creates our 4x4 grid of tiles by creating three
        # separate rows, each one containing 3 tiles
        #   - self: the Memory game to create a grid for
        self.grid_size = 4
        for i in range(self.grid_size):
            self.create_row()
        
    def create_row(self):
        # creates a single row in our grid of tiles. Each
        # row contains 3 tiles.
        #   - self: the TTT game to create a tile row for
        one_row = [ ]
        
        

        # calculate the dimensions that tiles need to be
        self.tile_width  = (self.window.get_width()-100) / self.grid_size
        self.tile_height = self.window.get_height() / self.grid_size

        # calculate the y-coordinates of tiles in this row.
        # To do so, we need to know what row number we are
        # creating tiles for. We can do that by taking the
        # current len of the grid, e.g., len 0 = first row
        row_index = len(self.grid)
        self.tile_y = self.tile_height * row_index

        # create each tile in the row. Tile x-coordinates are offset
        # by tile’s index (times tile width) in the row.
        
        
        for i in range(self.grid_size):
            self.tile_x = self.tile_width * i
            
            one_row.append(Tile(self.tile_x, self.tile_y, self.tile_width, self.tile_height, self.images[row_index*4 + i]))
            #pass

        # add the newly created row to our grid of tiles
        self.grid.append(one_row)
    
    def draw_score(self):
        # Draws the scoreboard on the window in the top left corner
        #   - self: is the game to draw the score for
        self.window.set_font_size(60)
        self.window.set_font_color("white")
        y = 0
        window_width  = 500
        
        scoreboard = str(self.score)
        xright = window_width - self.window.get_string_width(scoreboard)
        self.window.draw_string(scoreboard, xright, y)  
        
   
    
    
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
        # close the game if someone has clicked on the close button
        if event.type == QUIT:
            self.close_clicked = True

        # obtain position of mouse: event.pos
        # go over each tile and see if it overlaps with the position
        # if tile overlaps with event.pos, update tile content  
        if event.type == MOUSEBUTTONUP and self.continue_game == True:
            for row in self.grid:
                for tile in row:
                    tile.select(event.pos)

    def draw(self):
        # Draw all game objects.
        # - self is the Game to draw        
        self.window.clear()
        window_size = self.window.get_surface().get_size()
        self.draw_score()
        
        
        # draw each of our tiles
        for row in self.grid:
            for tile in row:
                tile.draw()
                
                
        

        self.window.update()
        
        
    def update(self):
        # Update the game objects.
        # - self is the Game to update
        self.score = pygame.time.get_ticks()//1000
             
    def decide_continue(self):
        # Check and remember if the game should continue
        # - self is the Game to check
        if Tile.tile_clicked == 16:
            self.continue_game = False



class Tile:
    # represents a single on a Tic Tac Toe board    
    
    border_width = 5
    fg_color = 'black'
    bg_color = 'black'
    tile_clicked = 0
    hidden_image = pygame.image.load('image0.bmp')
    window = None
    
    @classmethod    
    def set_window(cls, window):
        cls.window = window
        
    def __init__(self, x, y, width, height, images):
        # Create an object representing a tile on a TTT board.
        # x, y, width, and height specify a rectangle that
        # defines the perimiter of the tile.

        # create our instance attributes
        self.tile_exposed = False
        self.images = images
        self.rect = pygame.Rect(x, y, width, height)
    
        
    def draw(self):
        # draws our tile contents and borders to the screen
        #   - self: the tile to draw
        
        # draw our rectangle with borders
        rect_color = pygame.Color(self.fg_color)
        pygame.draw.rect(self.window.get_surface(), rect_color, self.rect, self.border_width)
        window_size = self.window.get_surface().get_size()
        if not self.tile_exposed:
            self.window.get_surface().blit(Tile.hidden_image, self.rect) 
        else:
            self.window.get_surface().blit(self.images, self.rect)
        
    
    def select(self, pos):
        # checks if the mouse is within the boundary of our tile.
        # if so, updates the contents of the tile.
        #   - self: the tile to update
        #   - pos: the position of the mouse when it was clicked
        
        # if the player has clicked outside of our boundaries,
        # ignore the click and do nothing
        if self.rect.collidepoint(pos) and not self.tile_exposed:
            self.tile_exposed = True
            Tile.tile_clicked += 1
        
    
main()