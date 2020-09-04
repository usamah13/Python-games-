# Tic Tac Toe Version 1
# 
# 3x3 grid of rectangles are displayed. There are two
# players, one X, one O. X goes first and players take
# turns clicking on tiles. The player's letter appears on
# an empty tile when clicked. If three of the same letters
# appear in a row, the corresponding player wins.
#
# Version 1 implements: drawing of the 9 tiles, and the
# ability to click on a tile to set its content to 'X'. Only
# one player exists in version 1.
import time, pygame
from uagame import Window
from pygame.locals import *

# User-defined functions
def main():
    # Creates the game window and game, and runs game

    window = Window('Tic Tac Toe', 500, 400)
    window.set_auto_update(False)
    game = Game(window)
    game.play()
    window.close()

# User-defined classes

class Game:
    # Defines a game of Tic Tac Toe

    def __init__(self, window):
        # Initialize a Game.
        # - self is the Game to initialize
        # - window is the uagame window object
        
        # create all of the game attributes
        self.window = window
        self.pause_time = 0.04 # smaller is faster game
        self.close_clicked = False
        self.continue_game = True        
        self.player1_shape = 'X'
        self.grid = [ ]
        self.create_grid()
        
    def create_grid(self):
        # creates our 3x3 grid of tiles by creating three
        # separate rows, each one containing 3 tiles
        #   - self: the TTT game to create a grid for
        for i in range(3):
            self.create_row()
        
    def create_row(self):
        # creates a single row in our grid of tiles. Each
        # row contains 3 tiles.
        #   - self: the TTT game to create a tile row for
        one_row = [ ]

        # calculate the dimensions that tiles need to be
        tile_width  = self.window.get_width() / 3
        tile_height = self.window.get_height() / 3

        # calculate the y-coordinates of tiles in this row.
        # To do so, we need to know what row number we are
        # creating tiles for. We can do that by taking the
        # current len of the grid, e.g., len 0 = first row
        row_index = len(self.grid)
        tile_y = tile_height * row_index

        # create each tile in the row. Tile x-coordinates are offset
        # by tile’s index (times tile width) in the row.
        for i in range(3):
            tile_x = tile_width * i
            one_row.append(Tile(100, 3, 'white', 'black', self.window, tile_x, tile_y, tile_width, tile_height))
            pass

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
        if event.type == MOUSEBUTTONUP and self.continue_game == True:
            for row in self.grid:
                for tile in row:
                    tile.select(event.pos)

    def draw(self):
        # Draw all game objects.
        # - self is the Game to draw        
        self.window.clear()
        
        # draw each of our tiles
        for row in self.grid:
            for tile in row:
                tile.draw()

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

    def __init__(self, content_size, border_width, fg_color, bg_color, window, x, y, width, height):


        # attributes related to drawing our rectangle
        self.rect = pygame.Rect(x, y, width, height)
        self.border_width = border_width

        # attributes related to drawing our tile content
        self.content_size = content_size
        self.content = ''
        
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
        
        # draw our content (if any)
        if self.content != '':
            self.window.set_font_size(self.content_size)
            self.window.set_font_color(self.fg_color)        
            x = self.rect.left + self.rect.width / 2 - self.window.get_string_width(self.content)/2
            y = self.rect.top + self.rect.height / 2 - self.window.get_font_height() / 2
            self.window.draw_string(self.content, x, y)
    
    def select(self, pos):
        # checks if the mouse is within the boundary of our tile.
        # if so, updates the contents of the tile.
        #   - self: the tile to update
        #   - pos: the position of the mouse when it was clicked
        
        # if the player has clicked outside of our boundaries,
        # ignore the click and do nothing
        if not self.rect.collidepoint(pos):
            # do nothing
            pass
        # tile is currently empty
        elif self.content == '':
            self.content = 'X'
        # otherwise, tile is already occupied
        else:
            # we need to flash the screen in a later version
            pass

    
main()