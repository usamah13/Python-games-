# Assignemnt 3:
# War Game is a card game that is played by 2 or more players with a deck of 52 cards. 
# The goal of this game is to be the first player to win all 52 cards.  

import random
class CircularQueue:
# Constructor, which creates a new empty queue:
    def __init__(self, capacity):
        if type(capacity) != int or capacity<=0:
            raise Exception ('Capacity Error')
        self.items = []
        self.capacity = capacity
        self.count=0
        self.head=0
        self.tail=0
        
# Adds a new item to the back of the queue, and returns nothing:
    def enqueue(self, item):
        if self.count== self.capacity:
            raise Exception('Error: Queue is full')
        if len(self.items) < self.capacity:
            self.items.append(item)
        else:
            self.items[self.tail]=item
        self.count +=1
        self.tail=(self.tail +1) % self.capacity
        
# Removes and returns the front-most item in the queue.
# Returns nothing if the queue is empty.
    def dequeue(self):
        if self.count == 0:
            raise Exception('Error: Queue is empty')
        item= self.items[self.head]
        self.items[self.head]=None
        self.count -=1
        self.head=(self.head+1) % self.capacity
        return item
        
# Returns the front-most item in the queue, and DOES NOT change the queue.
    def peek(self):
        if self.count == 0:
            raise Exception('Error: Queue is empty')
        return self.items[self.head]
        
# Returns True if the queue is empty, and False otherwise:
    def isEmpty(self):
        return self.count == 0
        
# Returns True if the queue is full, and False otherwise:
    def isFull(self):
        return self.count == self.capacity
        
# Returns the number of items in the queue:
    def size(self):
        return self.count
        
# Returns the capacity of the queue:
    def capacity(self):
        return self.capacity

# Removes all items from the queue, and sets the size to 0
# clear() should not change the capacity
    def clear(self):
        self.items = []
        self.count=0
        self.head=0
        self.tail=0
        
# Returns a string representation of the queue:
    def __str__(self):
        str_exp = "]"
        i=self.head
        for j in range(self.count):
            str_exp += str(self.items[i]) + " "
            i=(i+1) % self.capacity
        return str_exp + "]"   
    
# # Returns a string representation of the object CircularQueue
    def __repr__(self):
        return str(self.items) + ' Head=' + str(self.head) + ' Tail='+str(self.tail) + ' ('+str(self.count)+'/'+str(self.capacity)+')'
# START WRITING YOUR PROGRAM HERE
def read_and_validate_cards():
    #_function to read the file, and make a list(cards) containing all the string obejects representing the cards
    #_ This function also rasises exceptions to the main when the file doesn't have enough cards, duplicates, or wrong format
    #_Also makes the card's suit uppercase 
    
    
    #Reading the file and creating the list of cards
    
    filename = input ('Enter name of file to read >')
    file_object = open(filename, 'r')
    line = file_object.readline()
    cards = []
    while line:
        if line != '\n':
            cards.append(line.rstrip('\n').upper())
        line = file_object.readline()
    file_object.close()
    
    #Checking if the cards list is 52 or not
    
    if (len(cards) != 52):
        raise Exception('Error : Number of cards in the file is ' + str(len(cards)))
    
    
    duplicateHash = {}
    duplicates = []
    nonFormats = []
    for item in cards:
        if len(item) != 2 and item not in nonFormats:
            nonFormats.append(item)
        if item in duplicateHash and item not in duplicates:
            duplicates.append(item)
        else:
            duplicateHash[item] = True
            
    #Checking if the file has any duplicates by making a dictonary
    
    if (len(duplicates))!=0:
        stringDuplicate = ""
        for duplicate in duplicates:
            stringDuplicate = stringDuplicate + duplicate + ','
        raise Exception('Error: Duplicates found in the input file: ' + stringDuplicate.rstrip(','))
    
    #Checking if the file has any wrong format by making a dictonary
    
    if (len(nonFormats))!=0:
        stringNonFormat = ""
        for nonFormat in nonFormats:
            stringNonFormat = stringNonFormat + nonFormat + ','
        raise Exception('Error: Following cards not formatted correctly: ' + stringNonFormat.rstrip(','))
    
    
    return cards



def distribute_cards(cards):
    # Task 2 Distributing cards
    # Creates Two circular Queues(represstenting player1 and player2 and return them
    # - cards is a list of valid cards that has been read from the file
    
      
    # Created two circular queues for plyaer 1 and 2 respectively
    player1 = CircularQueue(52)
    player2 = CircularQueue(52)
    
    #choice is so we randomly decide which player to start giving the cards to first
    players =[player1, player2]
    choice = random.choice(players)
    
    
    #loop so the choice(chosen player) gets the first card and the other one gets the seconds card, 
    #we keep doing this till all the 52 cards are divided between the players equally.
    #Each player will have 26 cards after this loop
    i=0
    while i < len(cards):
        if choice == player1:
            player1.enqueue(cards[i])
            player2.enqueue(cards[i+1])
        else:
            player2.enqueue(cards[i])
            player1.enqueue(cards[i+1])            
        i+=2    
        
    return player1,player2
    

def get_user_input():
    # Task 3 Asking user for input
    # prompt the user to enter the number of cards that would be facedown for war
    # will repeatedly ask the user to enter a valid value if any number other than 1 or 2 or 3
    # is entered
    # returns the number entered by the user
    
    # loop to make sure it keeps asking for a valid input, 
    # only if a 1,2,3 is entered it breaks the loop and returs the number entered.
    
    correctInput = False
    while not correctInput:
        inputString = input('Enter the number of cards down ?')
        if inputString.isdigit():
            if int(inputString) not in (1,2,3):
                correctInput = False
            else:
                correctInput = True
                number = int(inputString)
        else:
            correctInput = False

    return number

def compare_cards(card1,card2):
    # Task 4 Comparing Cards
    # compares card1 of player 1 with card2 of player2
    # if card1 has higher rank return 1
    # if card2 has higher rank return 2
    # if card1 is equal to card2 reurn 0
    # - card 1 is a string representing a card of player1
    # - card 2 is a string representing a card of player2
    
    
    # added the cards into an empty list twocards, and also made a empty list with cardsrank 
    firstchar =0
    twocards = []
    twocards.append(card1)
    twocards.append(card2)
    cardsrank =[]
    
    # Made a loop so that first charcter of every card is ranked acoording to integers values, the integer values are then added to cardsrank list
    for card in twocards:
        
        if card[firstchar] == 'A':
            cardsrank.append(12)
            
        elif card[firstchar] == 'K':
            cardsrank.append(11)
        
        elif card[firstchar] == 'Q':
            cardsrank.append(10)  
            
        elif card[firstchar] == 'J':
            cardsrank.append(9)
            
        elif card[firstchar] == '0':
            cardsrank.append(8)  
            
        elif card[firstchar] == '9':
            cardsrank.append(7) 
            
        elif card[firstchar] == '8':
            cardsrank.append(6)    
            
        elif card[firstchar] == '7':
            cardsrank.append(5) 
            
        elif card[firstchar] == '6':
            cardsrank.append(4)      
               
        elif card[firstchar] == '5':
            cardsrank.append(3) 
            
        elif card[firstchar] == '4':
            cardsrank.append(2) 
            
        elif card[firstchar] == '3':
            cardsrank.append(1)
            
        elif card[firstchar] == '2':
            cardsrank.append(0) 

    #Here I compare the rank of each coressponding card and return the desired int value
    card1rank = cardsrank[0]
    card2rank = cardsrank[1]
    if card1rank > card2rank:
        return 1
    elif card2rank > card1rank:
        return 2
    else:
        return 0

class onTable:
    # Task 5  Create a class to represent the table
    # an instance of this class represents the table
    def __init__(self):
        # self is the onTable object
        # self.cards_list - is an object of type list that will contain objects of type str.  Each str object represent a card.
        # self.faceUp_list- an object of type list that contain objects of type bool. The bool object at a certain position in the self.faceUp_list is True if a card at the corresponding position in cards_list is faceup and False if a card is facedown.
        self.cards_list = []
        self.faceUp_list =[]



    def place(self,player,card,hidden):
        # places the given card on the table
        # -self is the onTable object
        # -player is an object of type int. It is 1 for player1 or 2 for player2
        # -card is an object of type str. It is the card being placed on the table
        # -hidden is an object of type bool. False when the card is faceup and True when facedown
        
        # Here the self.cards_list and self.faceUp_list are updated, based on the cards placed on the table, and whether or not they faceUp or are faceingDown
        # Insterting the cards of player1 so they go on the left side of the list and appending for player2 cards so that they are on the right side of the list 
        
        left = 0
        if player == 1 and hidden == False:
            self.cards_list.insert(left,card)
            self.faceUp_list.insert(left, hidden)
        elif player == 2  and hidden == False:
            self.cards_list.append(card)
            self.faceUp_list.append(hidden)
        elif player == 1 and hidden == True:
            self.cards_list.insert(left,card)
            self.faceUp_list.insert(left, hidden)
        elif player == 2  and hidden == True:
            self.cards_list.append(card)
            self.faceUp_list.append(hidden)

    def cleanTable(self):
        # cleans the table by initializing the instance attributes
        # -self is the onTable object
        # shuffles the card on the Table and then returns those ranodmized cards while also resetting the self.cards_list and self.faceUp_list
        
        random.shuffle(self.cards_list)
        card_list = self.cards_list
        self.cards_list =[]
        self.faceUp_list = []
        return card_list


    def __str__(self):
        # returns the representation of the cards on the table
        # -self is the onTable object
        # It give assignments desired str representation of the cards on the table

        cardslist_seprated = self.cards_list
        faceUpList = self.faceUp_list
        lengthOfTable = int(len(self.cards_list) / 2)
        
        i=0
        str_exp = "["
        while i < lengthOfTable:
            if not faceUpList[i]:
                str_exp += str(cardslist_seprated[i]) + ", "
            else:
                str_exp += "XX" + ", "
            i = i + 1
        str_exp = str_exp.rstrip(', ') + " | "
        
        while i < len(self.cards_list):
            if not faceUpList[i]:
                str_exp += str(cardslist_seprated[i]) + ", "
            else:
                str_exp += "XX" + ", "
            i = i + 1
        
        return str_exp.rstrip(', ') + "]"


def main():
    # try to read and validate the file, If any errrors caught, they will be printed here and the program ends
    try:
        cards = read_and_validate_cards()
    except IOError:
        print('Incorrect filename or file does not exist')
        
    except Exception as e: 
        print(e)
       
    #Game Starts here    
    else:
        
        # Cards distrubed to each player, each player is represent by a Circular queue
        # The number of cards to be faced down during war is also asked here
        # A class reprsenting the cards on the table is also created.
        
        player1cards,player2cards = distribute_cards(cards)
        facedownnumber = get_user_input()
        endGame = False
        cardsonTable = onTable()
        
        
        while not endGame:
            
            # Each player puts two cards facing up on the table
            faceUpCard1 = player1cards.dequeue()
            cardsonTable.place(1,faceUpCard1,False)
            faceUpCard2 = player2cards.dequeue()
            cardsonTable.place(2,faceUpCard2,False)
            
            # cards on the table displayed and the amount of cards that each player has in their hands is displayed
            print(cardsonTable)
            print("Player 1: " + str(player1cards.size()) + " Player 2: " + str(player2cards.size()))
            
            
            # the ranks of each players faced up card is compared
            # based on the comparsion either player 1 gets all the cards in the table(if player 1 has a higher rank card)
            # or player 2 takes them. (if player 2 has a higher rank card)
            comparision = compare_cards(faceUpCard1, faceUpCard2)
            if comparision == 1:
                cardsWon = cardsonTable.cleanTable()
                for item in cardsWon:
                        player1cards.enqueue(item)
                print("Player1 takes all the cards on the table")
            elif comparision == 2:
                cardsWon = cardsonTable.cleanTable()
                for item in cardsWon:
                        player2cards.enqueue(item)
                print("Player2 takes all the cards on the table")
                
            
            # If both players have the same rank cards then war starts
            else:
                print("WAR STARTS!!!")
                
                
                # dequing the amount of cards facing downwards as the user specified before, and making sure they have enough cards to put on the in their hands
                i = 0
                while i < facedownnumber and player1cards.size() > facedownnumber:
                    faceDownCard1 = player1cards.dequeue()
                    cardsonTable.place(1,faceDownCard1,True)
                    i =  i + 1
                
                if player1cards.size() < facedownnumber:
                   # END GAME PLAYER 2 WINs, when player1 has no more cards to give out so player2 takes cards on the table and player1's cards 
                    cardsWar = cardsonTable.cleanTable()
                    for item in cardsWar:
                        player2cards.enqueue(item)
                    while not player1cards.isEmpty():
                        player2cards.enqueue(player1cards.dequeue())
                    print("Player1 does not have enough cards!")
                    print("Player2 takes all cards on table and player 1 cards")
                    endGame = True
                
                else:
                   # END GAME PLAYER 1 WINs,  when player2 has no more cards to give out so player1 takes cards on the table and player2's cards
                    i = 0
                    while i < facedownnumber and player2cards.size() > facedownnumber:
                        faceDownCard2 = player2cards.dequeue()
                        cardsonTable.place(2,faceDownCard2,True)
                        i = i + 1
                    if player2cards.size() < facedownnumber:
                        cardsWar = cardsonTable.cleanTable()
                        for item in cardsWar:
                            player1cards.enqueue(item)
                        while not player2cards.isEmpty():
                            player1cards.enqueue(player2cards.dequeue())
                        print("Player2 does not have enough cards!")
                        print("Player1 takes all cards on table and player 2 cards")
                        endGame = True
            
            # printing the 60 dashes and enter to go on to the next round I followed the sample output file  not the image on eclass, since it has a space between the dashes and next round
            pressEnter = input(60*"-")
            
            # end game if any player has zero cards
            if player1cards.isEmpty() or player2cards.isEmpty():
                endGame = True
        
        # displaying the player who won
        winner = ""
        if player1cards.size() > player2cards.size():
            winner = "Player1 won"
        else:
            winner = "Player2 won"
        print(winner)
        print("Player1: " + str(player1cards.size()) + " Player2: " + str(player2cards.size()))
main()