# Assignment 2
#2048 is a single-player sliding block puzzle game. 
#The game's objective is to slide numbered tiles typically on a 4x4 grid to combine them to create a tile with the number 2048. 
#The tiles are slid all together either upwards, downwards, left or right and go all together to one side of the grid, stopped only by either the border of the grid or a neighbouring filled tile. 
#Two adjacent tiles in the same direction of the slide with the same values are summed in one tile. 
#A tile participates in a merge only once in each round. At each round, a new empty tile is filled with a 2 or 4 and the player slides the tiles of the board in one direction (up, down, left or right) again. 
#The player wins if the value 2048 is reached, and loses if all the tiles are filled and no sliding is possible.


# Set the row and column in both grid and game class to decide the grid size

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
        # Creates the grid here using the arguments row and col as the number of rows and columns of the grid to be made.
        # returns the grid in the end
         # self is the Grid object 

        grid = []      

        for row_index in range(row): 
            rowlist = []
            for colmn_index in range(col):
                rowlist.append(0)       # Intialiazing all the rows and coulmns to be empty in the grid
            grid.append(rowlist)
        return grid


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
        # This function updates the list of empty tiles of the grid.
        # self is the Grid object 
        # self.empies Set is the list of tiles which are empty

        self.emptiesSet = []
        rowindex = 0
        for x in self.grid: # x is the whole row 
            for y in range(len(x)): # y is coulmn number 
                coordinate = []
                if x[y] == 0:   #if the tile is empty
                    coordinate.append(rowindex)
                    coordinate.append(y)
                    self.emptiesSet.append(coordinate)
            rowindex += 1

    def collapsible(self):
        
        #This function cheks if the grid of the game is collapsible in any direction (left, right, up or down.)
        # It returns True if the grid is collapsible and False otherwise 
        # self is the Grid object
        # return colapible as soon as the any of the if or else condition is met

        self.updateEmptiesSet()  # make sure the lates empties set list is checked 
        collapsible = False

        if len(self.emptiesSet) > 0: # if any empty tile collapsible condidtion is met 
            collapsible = True
            return collapsible
        else:
            
            for rowindex in range(len(self.grid)): 
                lastRow = len(self.grid) - 1
                
                if rowindex == lastRow:  # if its the last row we don't need to check if the element can be collapsed up or down since that was done for this row in the else clause
                    
                    for z in range(len(self.grid[lastRow])):    # z is the (column index)
                        cur = self.grid[lastRow][z]             # current elment of the row
                        hasNext = z + 1                           # the element after the current one
                        
                        if hasNext >= len(self.grid[lastRow]): # if you are the last elment of the row then loop breaks becuse no element after it 
                            break
                       
                        elif cur == self.grid[lastRow][hasNext]: # if they are next elment and current elment are the same collapsible condition met 
                            collapsible = True
                            return collapsible
                else:
                    # For all the other rows, checking if it is collapsible
                    
                    for col_index in range(len(self.grid[rowindex])): # the column 
                        cur = self.grid[rowindex][col_index]
                        hasNext = col_index +1
                        
                        if hasNext >= len(self.grid[rowindex]):
                            if cur == self.grid[rowindex + 1][col_index]: # comparing the last element of the row to the bottom elment 
                                collapsible = True
                                return collapsible
                            break
                       
                        elif cur == self.grid[rowindex][hasNext] or cur == self.grid[rowindex + 1][col_index]: # checking each current elemment with its left and bottom element 
                            collapsible = True
                            return collapsible

        return collapsible

    def collapseRow(self, lst): 
        #This function takes a list lst and collapses it to the LEFT.
    
        #This function should return two values:
        #1. the collapsed list and
        #2. True if the list is collapsed and False otherwise.        
        # self is the Grid object
        # found something like this from stackoverflow, and used the same steps as in that algorithm 

        curValue = None
        collapsed = False
        collapsedlst = []
        
        for nextValue in lst: 
            if not nextValue: # if empty tile skip
                continue
            
            if curValue is None: # if no value has been set, set current as next value (which is the current element)
                curValue = nextValue
                
            elif curValue == nextValue: # if the current element is equal to next elemenyt then merge them and update score and  and update the collapsewd list and reset the current value
                collapsedlst.append(curValue + nextValue)
                self.score = self.score + (curValue + nextValue)
                curValue = None
                
            else: # otherwise just add the elements to the collapsed list and set current value to the next value
                collapsedlst.append(curValue)
                curValue = nextValue
                
        if curValue is not None: # for the last element in the list 
            collapsedlst.append(curValue)
        collapsedlst.extend([0] * (len(lst) - len(collapsedlst))) # append the remaining zeros(empty tiles) to complete the list if needed

        if collapsedlst != lst: # if the collapsed list is not equal to the orignallist then that means the numbers have merged and collapsable can be set true
            collapsed = True
            
        else:
            collapsed = False
        return (collapsedlst, collapsed)



    def collapseLeft(self):
        
        #This function uses collapseRow() to collapse all the rows in the grid to the LEFT.
    
        #This function should return True if any row of the grid is collapsed and False otherwise.  
        
        # self is the Grid object
        
        
        newGrid = []
        anyCollapsed = False
        for row in self.grid:
            collapsedlst, collapsed = self.collapseRow(row)
            if collapsed:
                anyCollapsed = True
            newGrid.append(collapsedlst)
        self.grid = newGrid    # updated grid

        return anyCollapsed




    def collapseRight(self):
        
        #This function uses collapseRow() to collapse all the rows in the grid to the RIGHT.
    
        #This function should return True if any row of the grid is collapsed and False otherwise.  
        

        # self is the Grid object
        
        newGrid = []
        anyCollapsed = False
        for row in self.grid:
            row.reverse()        # reversing it so that we collapse it towards the right 
            collapsedlst, collapsed = self.collapseRow(row)
            if collapsed:
                anyCollapsed = True
            collapsedlst.reverse()     # reversing the collapsed list so that end result is fine in the grid  
            newGrid.append(collapsedlst)
        self.grid = newGrid

        return anyCollapsed



    def collapseUp(self):
        
        #This function uses collapseRow() to collapse all the columns in the grid to the upwards.
    
        #This function should return True if any coulumn of the grid is collapsed and False otherwise.  
        

        # self is the Grid object        

        columnGrid = []
        columnCount = 0
        
        # making the grid column wise( so each column becomes the row )
        for y in range(self.col): 
            column = []
            for x in range(self.row):
                column.append(self.grid[x][columnCount])
            columnCount = columnCount + 1
            columnGrid.append(column)
            
        # the same as the collapse left methond because thats what we do when we want to collapse upwards
        newColumnGrid = []
        anyCollapsed = False
        for row in columnGrid:
            collapsedlst, collapsed = self.collapseRow(row)
            if collapsed:
                anyCollapsed = True
            newColumnGrid.append(collapsedlst)
            

        # Converting the Column wise grid back to row wise the orginal sturcture 
        newGrid = []
        columnCount = 0
        for y in range(self.col):
            column = []
            for x in range(self.row):
                column.append(newColumnGrid[x][columnCount])
            columnCount = columnCount + 1
            newGrid.append(column)

        self.grid = newGrid

        return anyCollapsed



    def collapseDown(self):
        
        #This function uses collapseRow() to collapse all the columns in the grid to the downwards.
    
        #This function should return True if any coulumn of the grid is collapsed and False otherwise.  
        

        # self is the Grid object 
        
        columnGrid = []
        columnCount = 0
        # making the grid column wise( so each column becomes the row )
        for y in range(self.col):
            column = []
            for x in range(self.row):
                column.append(self.grid[x][columnCount])
            columnCount = columnCount + 1
            columnGrid.append(column)

        # the same as the collapse right methond because thats what we do when we want to collapse downwards
        newColumnGrid = []
        anyCollapsed = False
        for row in columnGrid:
            row.reverse()
            collapsedlst, collapsed = self.collapseRow(row)
            if collapsed:
                anyCollapsed = True
            collapsedlst.reverse()
            newColumnGrid.append(collapsedlst)
        
        
        # Converting the Column wise grid back to row wise the orginal sturcture 
        newGrid = []
        columnCount = 0
        for y in range(self.col):
            column = []
            for x in range(self.row):
                column.append(newColumnGrid[x][columnCount])
            columnCount = columnCount + 1
            newGrid.append(column)

        self.grid = newGrid

        return anyCollapsed


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
