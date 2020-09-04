import random as rnd
import os
import sys

class Grid():
    def __init__(self, row=4, col=4, initial=2):
        self.row = row                              # number of rows in grid
        self.col = col                              # number of columns in grid
        self.initial = initial                      # number of initial cells filled
        self.score = 0

        self.grid = self.createGrid(row, col)       # creates the grid specified above

        self.emptiesSet = []                        # list of empty cells
        self.updateEmptiesSet()

        for _ in range(self.initial):               # assign two random cells
            self.assignRandCell(init=True)


    def createGrid(self, row, col):

        """
        Create the grid here using the arguments row and col
        as the number of rows and columns of the grid to be made.

        The function should return the grid to be used in __init__()
        """

        pass


    def assignRandCell(self, init=False):

        """
        This function assigns a random empty cell of the grid
        a value of 2 or 4.

        In __init__() it only assigns cells the value of 2.

        The distribution is set so that 75% of the time the random cell is
        assigned a value of 2 and 25% of the time a random cell is assigned
        a value of 4
        """

        if len(self.emptiesSet):
            cell = rnd.sample(self.emptiesSet, 1)[0]
            if init:
                self.grid[cell[0]][cell[1]] = 2
            else:
                cdf = rnd.random()
                if cdf > 0.75:
                    self.grid[cell[0]][cell[1]] = 4
                else:
                    self.grid[cell[0]][cell[1]] = 2
            self.emptiesSet.remove(cell)


    def drawGrid(self):

        """
        This function draws the grid representing the state of the game
        grid
        """

        for row_index in range(self.row):
            line = '\t|'
            for col_index in range(self.col):
                if not self.grid[row_index][col_index]:
                    line += ' '.center(5) + '|'
                else:
                    line += str(self.grid[row_index][col_index]).center(5) + '|'
            print(line)
        print()


    def updateEmptiesSet(self):

        """
        This function should update the list of empty tiles of the grid.
        """

        pass


    def collapsible(self):

        """
        This function should test if the grid of the game is collapsible
        in any direction (left, right, up or down.)

        It should return True if the grid is collapsible.
        It should return False otherwise.
        """

        pass



    def collapseRow(self, lst):

        """
        This function takes a list lst and collapses it to the LEFT.

        This function should return two values:
        1. the collapsed list and
        2. True if the list is collapsed and False otherwise.
        """

        pass



    def collapseLeft(self):

        """
        This function should use collapseRow() to collapse all the rows
        in the grid to the LEFT.

        This function should return True if any row of the grid is collapsed
        and False otherwise.
        """

        pass



    def collapseRight(self):

        """
        This function should use collapseRow() to collapse all the rows
        in the grid to the RIGHT.

        This function should return True if any row of the grid is collapsed
        and False otherwise.
        """

        pass



    def collapseUp(self):

        """
        This function should use collapseRow() to collapse all the columns
        in the grid to UPWARD.

        This function should return True if any column of the grid is
        collapsed and False otherwise.
        """

        pass



    def collapseDown(self):

        """
        This function should use collapseRow() to collapse all the columns
        in the grid to DOWNWARD.

        This function should return True if any column of the grid is
        collapsed and False otherwise.
        """

        pass


class Game():
    def __init__(self, row=4, col=4, initial=2):
        self.game = Grid(row, col, initial)
        self.play()


    def printPrompt(self):
        if sys.platform == 'win32':
            os.system("cls")
        else:
            os.system("clear")
        print('Press "w", "a", "s", or "d" to move Up, Left, Down or Right respectively.')
        print('Enter "p" to quit.\n')
        self.game.drawGrid()
        print('\nScore: ' + str(self.game.score))


    def play(self):

        moves = {'w' : 'Up',
                 'a' : 'Left',
                 's' : 'Down',
                 'd' : 'Right'}

        stop = False
        collapsible = True

        while not stop and collapsible:
            self.printPrompt()
            key = input('\nEnter a move: ')

            while not key in list(moves.keys()) + ['p']:
                self.printPrompt()
                key = input('\nEnter a move: ')

            if key == 'p':
                stop = True
            else:
                move = getattr(self.game, 'collapse' + moves[key])
                collapsed = move()

                if collapsed:
                    self.game.updateEmptiesSet()
                    self.game.assignRandCell()

                collapsible = self.game.collapsible()

        if not collapsible:
            if sys.platform == 'win32':
                os.system("cls")
            else:
                os.system("clear")
            print()
            self.game.drawGrid()
            print('\nScore: ' + str(self.game.score))
            print('No more legal moves.')


# -----------------------------------------------------------------------------
# Main Function ---------------------------------------------------------------
# -----------------------------------------------------------------------------


# This condition ensures that the game isn't run if the file is loaded as
# a module. Will only run if the file is executed.

if __name__ == '__main__':
    game = Game()
