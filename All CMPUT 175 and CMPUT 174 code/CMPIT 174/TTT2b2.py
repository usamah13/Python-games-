# Game Code Template
from uagame import Window
import time,random
import pygame
from pygame.locals import *

# User-defined functions

def main():

    window = Window('Tic Tac Toe', 500, 400)
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
        
        # Game Class always has the following 4 instance attributes
        self.window = window
        # Call the Class Method to set the Tile's window
        Tile.set_window(window)
        self.pause_time = 0.04 # smaller is faster game
        self.close_clicked = False
        self.continue_game = True
        self.player_1 = 'X'
        self.player_2 = 'O'
        self.turn = self.player_1
        self.filled =[]
        self.board = []
        self.flashers = []
        self.create_board()
    def create_board(self):
        width = self.window.get_width()//3
        height = self.window.get_height()//3
        for row_index in range(0,3):
            row =[]
            for col_index in range(0,3):
                x = width * col_index
                y = height * row_index
                tile = Tile(x,y,width,height)
                row.append(tile)
            self.board.append(row)
                
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
        if event.type == MOUSEBUTTONUP and self.continue_game:
            self.handle_mouse_up(event.pos)
    def handle_mouse_up(self,click_position):
        for row in self.board:
            for tile in row:
                if tile.select(click_position,self.turn):
                    self.filled.append(tile)
                    self.change_turn()
    def change_turn(self):
        if self.turn == self.player_1:
            self.turn = self.player_2
        else:
            self.turn = self.player_1

    def draw(self):
        # Draw all game objects.
        # - self is the Game to draw
        
        self.window.clear()
        # Code for drawing the objects should be written here
        self.choose_flashing_tile()
        for row in self.board:
            for tile in row:
                tile.draw()
        self.window.update()
    def choose_flashing_tile(self):
        if len(self.flashers) >0:
            tile = random.choice(self.flashers)
            tile.set_flashing_attribute() # sets self.flashing to True for the chosen Tile object
    def update(self):
        # Update the game objects.
        # - self is the Game to update
        # Write code for moving the Game object for the next frame
        pass
    def is_list_win(self,tile_list):
        # == operator is calling the __eq__ inside the Tile class
        if tile_list[0] == tile_list[1] == tile_list[2]:
            self.flashers = tile_list
            return True
        else:
            return False
    def is_diagonal_win(self):
        diagonal_win = False
        diagonal1 = [self.board[0][0],self.board[1][1],self.board[2][2]]
        diagonal2 = [self.board[0][2],self.board[1][1],self.board[2][0]]
        if self.is_list_win(diagonal1) or self.is_list_win(diagonal2):
            diagonal_win = True
        return diagonal_win
    def is_column_win(self):
        column_win = False
        for col_index in range(3):
            column = []
            for row_index in range(0,3):
                tile = self.board[row_index][col_index]
                column.append(tile)
            if self.is_list_win(column):
                return True
        #return column_win
    def is_row_win(self):
        row_win = False
        for row in self.board:
            if self.is_list_win(row):
                row_win = True
        return row_win
    def is_win(self):
        win = False
        if self.is_row_win() or self.is_column_win() or self.is_diagonal_win():
            win = True
        return win
    def is_tie(self):
        tie = False
        if len(self.filled) == 9:
            self.flashers = self.filled
            tie = True
        return tie
    def decide_continue(self):
        # Check and remember if the game should continue
        # - self is the Game to check
        # Write code to check if game should continue or not
        if self.is_win() or self.is_tie():
            self.continue_game  = False
class Tile:
    # Class Attributes
    fg_color = 'white'
    font_size = 133
    border_width = 3
    window= None
    # Class Methods
    @classmethod
    def set_window(cls,game_window):
        cls.window = game_window
    # Instance Methods
    def __init__(self,x,y,width,height):
        self.rect = pygame.Rect(x,y,width,height)
        self.flashing = False
        self.content = ''
    def __eq__(self,other_tile):
        if self.content != '' and self.content == other_tile.content:
            return True
        else:
            return False
    def set_flashing_attribute(self):
        self.flashing = True
    def draw(self):
        surface = Tile.window.get_surface()
        color = pygame.Color(Tile.fg_color)        
        if self.flashing:
            # draw a white recangle
            pygame.draw.rect(surface,color,self.rect,0)
            self.flashing = False
        else:
            # draw a black rectangle with a white border
            self.draw_content()
            pygame.draw.rect(surface,color,self.rect,Tile.border_width)
    def draw_content(self):
        # location,size, color
        Tile.window.set_font_size(Tile.font_size)
        Tile.window.set_font_color(Tile.fg_color)
        # Location
        string_width = Tile.window.get_string_width(self.content)
        string_height = Tile.window.get_font_height()
        content_x = self.rect.x + (self.rect.width - string_width)//2
        content_y = self.rect.y + (self.rect.height - string_height)//2
        Tile.window.draw_string(self.content,content_x,content_y)
    def select(self,position,player):
        valid_click = False
        if self.rect.collidepoint(position):    
            if self.content == '':
                self.content = player
                valid_click = True
            else:
                self.flashing = True
        return valid_click
    
    
main()
