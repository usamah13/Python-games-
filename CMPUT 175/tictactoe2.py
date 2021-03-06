class TicTacToe:
    def __init__(self):
        # "board" is a list of 10 strings representing the board (ignore index 0)
        self.board = [" "]*10
        self.board[0]="#"
        
#------------------------------------------------------------- 
    def drawBoard(self):
        # This method prints out the board with current plays adjacent to a board with index.
        #write some code here
        separator = "-"*11
        separator += "\t" + "-"*11
        separator += "\n"        
        topRow = "7 | 8 | 9\n"
        midRow = "4 | 5 | 6\n"
        botRow = "1 | 2 | 3"

        stringToDisplay = " " + self.board[7] + " | " + self.board[8] + " | " + self.board[9] + "\t" + topRow + separator
        stringToDisplay += " " + self.board[4] + " | " + self.board[5] + " | " + self.board[6] + "\t" + midRow + separator
        stringToDisplay += " " + self.board[1] + " | " + self.board[2] + " | " + self.board[3] + "\t" + botRow

        print(stringToDisplay)

#------------------------------------------------------------- 
    def boardFull(self):
    # This method checks if the board is already full and returns True. Returns false otherwise
    #write some code here
        boardIsFull = False
        for element in self.board:
            if element == " ":
                boardIsFull = False
                return boardIsFull
            else:
                boardIsFull = True
        return boardIsFull

#------------------------------------------------------------- 
    def cellIsEmpty(self, cell):
    #write some code here
        if cell > 0 and cell < 10 and self.board[cell] == " ":
            return True
        else:
            return False

#------------------------------------------------------------- 
            

#-------------------------------------------------------------
    def assignMove(self, cell,symbol):
    # assigns the symbols to the cell in the board
        if cell > 0 and cell < 10:
            self.board[cell] = symbol
            return True
        else:
            return False

#write some code here

#------------------------------------------------------------- 
    def whoWon(self):
    # returns the symbol of the player who won if there is a winner, otherwise it returns an empty string. 
        if self.isWinner("x"):
            return "x"
        elif self.isWinner("o"):
            return "o"
        else:
            return ""

#-------------------------------------------------------------   
    def isWinner(self, symbol):
    # Given a player's letter, this method returns True if that player has won.
    #write some code here
        #rows
        if self.board[7] == symbol and self.board[8] == symbol and self.board[9] == symbol:
            return True
        elif self.board[4] == symbol and self.board[5] == symbol and self.board[6] == symbol:
            return True
        elif self.board[1] == symbol and self.board[2] == symbol and self.board[3] == symbol:
            return True
        #diganols 
        elif self.board[7] == symbol and self.board[5] == symbol and self.board[3] == symbol:
            return True
        elif self.board[1] == symbol and self.board[5] == symbol and self.board[9] == symbol:
            return True
        #colums:
        elif self.board[7] == symbol and self.board[4] == symbol and self.board[1] == symbol:
            return True
        elif self.board[8] == symbol and self.board[5] == symbol and self.board[2] == symbol:
            return True
        elif self.board[9] == symbol and self.board[6] == symbol and self.board[3] == symbol:
            return True        
        else:
            return False

def main():
      
    # Write your program here
    print("Welcome to Tic Tac Toe Series")
    playAgain = "y"

    while playAgain == "Y" or playAgain == "y":
        myBoard=TicTacToe()
        PLAYER_ONE = 'x'
        PLAYER_TWO = 'o'
        gameIsRunning = True
        myBoard.drawBoard()
        symbol = PLAYER_ONE
        
        def change_turn(symbol): # chaninging turn  
            #PLAYER_ONE = 'x'
            #PLAYER_TWO = 'o'            
            if symbol ==  PLAYER_ONE:
                symbol = PLAYER_TWO  
            elif symbol ==  PLAYER_TWO:
                symbol = PLAYER_ONE
            return symbol
        while gameIsRunning:
            #if symbol == PLAYER_ONE:
            playerOneIsValid = False
            playerOne = input("It is the turn for "+ symbol +". What is your move? ")
            while (playerOneIsValid == False):
                if myBoard.cellIsEmpty(int(playerOne)) and myBoard.assignMove(int(playerOne), symbol):
                    playerOneIsValid = True
                    myBoard.drawBoard()
                    if myBoard.whoWon() !="":
                        print(myBoard.whoWon()+" wins. Congrats!")
                        playerOneIsValid = True
                        gameIsRunning = False
                    else:
                        if myBoard.boardFull():
                            print("It's a tie.")
                            playerOneIsValid = True
                            gameIsRunning = False
                        else:
                            symbol = change_turn(symbol)
                            playerOneIsValid = True
                    
                else:
                    playerOneIsValid = False
                    if not (int(playerOne) > 0 and int(playerOne) < 10) :
                        playerOne = input("Invalid move. Turn for "+ symbol +" again.What is your move? ")
                    elif(not myBoard.cellIsEmpty(int(playerOne))):
                        playerOne = input(str(playerOne) + " is not available. Turn for "+ symbol +" again.What is your move? ")
                    else:
                        playerOne = input("Invalid move. Turn for "+ symbol +" again.What is your move? ")
        cont = input("Press Enter to continue ")
        while(cont != ''):
            cont = input("Press Enter to continue")
        playAgain = input("Do you want to play another game? (Y/N)")            

main()