# Memory Version 1
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
        
        self.grid = [ ]
        
        self.images = [ ]
        self.create_image_list()
        self.create_grid()
        
        
        
    def create_image_list(self):
        imagesname = [ ]
        for i in range(1,9):
            imgstr = 'image' +str(i)+ '.bmp'
            imagesname.append(imgstr)
            
        #imagesname = ['image1.bmp', 'image2.bmp', 'image3.bmp', 'image4.bmp', 'image5.bmp', 'image6.bmp' , 'image7.bmp' , 'image8.bmp' ]
        
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
            
            one_row.append(Tile( 5, 'black', 'black', self.window, self.tile_x, self.tile_y, self.tile_width, self.tile_height, self.images[row_index*4 + i]))
            #pass

        # add the newly created row to our grid of tiles
        self.grid.append(one_row)
        
   
    
    
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
        #if event.type == MOUSEBUTTONUP and self.continue_game == True:
            #for row in self.grid:
                #for tile in row:
                    #tile.select(event.pos)

    def draw(self):
        # Draw all game objects.
        # - self is the Game to draw        
        self.window.clear()
        window_size = self.window.get_surface().get_size()
        
        
        
        # draw each of our tiles
        for row in self.grid:
            for tile in row:
                tile.draw()
                #for i in range(0,16):
                    #screen.blit(self.images[i], (self.tile_x, self.tile_y))  

        self.window.update()
        
        
    def update(self):
        # Update the game objects.
        # - self is the Game to update
        pass
             
    def decide_continue(self):
        # Check and remember if the game should continue
        # - self is the Game to check
        pass



class Tile:
    # represents a single on a Tic Tac Toe board

    def __init__(self, border_width, fg_color, bg_color, window, x, y, width, height, image):

        self.image = image
        # attributes related to drawing our rectangle
        self.rect = pygame.Rect(x, y, width, height)
        self.border_width = border_width

        # attributes related to drawing our tile content
    
        
        # palette choices
        self.fg_color = fg_color
        self.bg_color = bg_color
        
        # the window to draw our tile to
        self.window = window
        
    def draw(self):
        # draws our tile contents and borders to the screen
        #   - self: the tile to draw
        
        # draw our rectangle with borders
        rect_color = pygame.Color(self.fg_color)
        pygame.draw.rect(self.window.get_surface(), rect_color, self.rect, self.border_width)
        window_size = self.window.get_surface().get_size()

        self.window.get_surface().blit(self.image, self.rect)        
        # draw our content (if any)
        
        #if self.content != '':
            #self.window.set_font_size(self.content_size)
            #self.window.set_font_color(self.fg_color)        
            #x = self.rect.left + self.rect.width / 2 - self.window.get_string_width(self.content)/2
            #y = self.rect.top + self.rect.height / 2 - self.window.get_font_height() / 2
            #self.window.draw_string(self.content, x, y)
    
    #def select(self, pos):
        # checks if the mouse is within the boundary of our tile.
        # if so, updates the contents of the tile.
        #   - self: the tile to update
        #   - pos: the position of the mouse when it was clicked
        
        # if the player has clicked outside of our boundaries,
        # ignore the click and do nothing
        #if not self.rect.collidepoint(pos):
            # do nothing
            #pass
        # tile is currently empty
        #elif self.content == '':
            #self.content = 'X'
        # otherwise, tile is already occupied
        #else:
            # we need to flash the screen in a later version
            #pass

    
main()