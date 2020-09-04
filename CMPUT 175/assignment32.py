# War Game 

import random
import sys
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
    filename = input ('Enter name of file to read >')
    file_object = open(filename, 'r')
    line = file_object.readline()
    cards = []
    while line:
        if line != '\n':
            cards.append(line.rstrip('\n').upper())
        line = file_object.readline()
    file_object.close()
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
    if (len(duplicates)):
        stringDuplicate = ""
        for duplicate in duplicates:
            stringDuplicate = stringDuplicate + duplicate + ','
        raise Exception('Error: Duplicates found in the input file: ' + stringDuplicate.rstrip(','))
    if (len(nonFormats)):
        stringNonFormat = ""
        for nonFormat in nonFormats:
            stringNonFormat = stringNonFormat + nonFormat + ','
        raise Exception('Error: Following cards not formatted correctly: ' + stringNonFormat.rstrip(','))
    #except IOError:
        #raise IOError('Incorrect filename or file does not exist')
    return cards
    #sys.exit()


def distribute_cards(cards):
    # Task 2 Distributing cards
    # Creates Two circular Queues and return them
    # - cards is a list of valid cards that has been read from the file
    # TODO
    
    #player1list = cards[:len(cards)//2]
    #player2list = cards[len(cards)//2:]    
    
    player1 = CircularQueue(52)
    player2 = CircularQueue(52)
    
    players =[player1, player2]
    choice = random.choice(players)
    
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
    # TODO
    
    number = int(input('Enter the number of cards down ?'))
    while number not in (1,2,3):
        number = int(input('Enter the number of cards down ?'))
         
    return number
        

def compare_cards(card1,card2):
    # Task 4 Comparing Cards
    # compares card1 of player 1 with card2 of player2
    # if card1 has higher rank return 1
    # if card2 has higher rank return 2
    # if card1 is equal to card2 reurn 0
    # - card 1 is a string representing a card of player1
    # - card 2 is a string representing a card of player2
    # TODO
    
    firstchar =0
    twocards = [card1,card2] 
    cardsrank =[]
    for card in twocards:
        
        if card[firstchar] == 'A':
            cardsrank.append(12)
            
        elif card[firstchar] == 'K':
            cardsrank.append(11)
        
        elif card[firstchar] == 'Q':
            cardsrank.append(10)  
            
        elif card[firstchar] == 'J':
            cardsrank.append(9)
            
        elif card[firstchar] == '10':
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
     
    print(cardsrank)
        
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
        # TODO
        self.cards_list = []
        self.face_uplist =[]
        
        
    
    def place(self,player,card,hidden):
        # places the given card on the table
        # -self is the onTable object
        # -player is an object of type int. It is 1 for player1 or 2 for player 2
        # -card is an object of type str. It is the card being placed on the table
        # -hidden is an object of type bool. False when the card is faceup and True when facedown
        # TODO
        
        #hiddenstr = 'XX'
        left = 0
        if player == 1 and hidden == False:
            self.cards_list.insert(left,card)
            self.face_uplist.insert(left, hidden)
        elif player == 2  and hidden == False:
            self.cards_list.append(card)
            self.face_uplist.append(hidden)
        
        elif player == 1 and hidden == True:
            self.cards_list.insert(left,card)
            self.face_uplist.insert(left, hidden)    
            
        elif player == 2  and hidden == True:
            self.cards_list.append(card)
            self.face_uplist.append(hidden)   
        
            
    def cleanTable(self):
        # cleans the table by initializing the instance attributes
        # -self is the onTable object
        # TODO
        
        shuffling = True 
        if shuffling:
            random.shuffle(self.cards_list)
            shuffling = False 
            return self.cards_list
        
        self.cards_list =[]
        self.face_uplist =[]        
        
    def __str__(self):
        # returns the representation of the cards on the table
        # -self is the onTable object
        # TODO
        
        cardslist_seprated = self.cards_list
        cardslist_seprated.insert((len(cardslist_seprated)//2),'|')
        str_exp = "["
        i=0
        for j in range(len(cardslist_seprated)):
            str_exp += str(cardslist_seprated[i]) + " "
            i=(i+1) % (len(cardslist_seprated))
        return str_exp + "]"           


def main():
    # TODO - IMPLEMENT ALGORITHM HERE
    try:
        cards = read_and_validate_cards()
    except IOError:
        print('Incorrect filename or file does not exist')
        #sys.exit()
    except Exception as e: 
        print(e)
        #sys.exit()
        
    else:
    
        player1cards,player2cards = distribute_cards(cards)
        facedownnumber = get_user_input()
        endGame = False
        cardsonTable = onTable()
        while not endGame:

            faceUpCard1 = player1cards.dequeue()
            cardsonTable.place(1,faceUpCard1,False)
            faceUpCard2 = player2cards.dequeue()
            cardsonTable.place(2,faceUpCard2,False)
            print(cardsonTable)
            print("Player 1: " + str(player1cards.size()) + " Player 2: " + str(player2cards.size()))
            print("FACE UP CARD 1: " + str(faceUpCard1))
            print("FACE UP CARD 2: " + str(faceUpCard2))
            comparision = compare_cards(faceUpCard1, faceUpCard2)
            if comparision == 1:
                cardsWon = cardsonTable.cleanTable()
                for item in cardsWon:
                    player1cards.enqueue(item)
                print("Player 1 takes all the card on the table")
            elif comparision == 2:
                cardsWon = cardsonTable.cleanTable()
                for item in cardsWon:
                    player2cards.enqueue(item)
                print("Player 2 takes all the card on the table")
            else:
                print("WAR STARTS!!!")
                faceDownCard1 = player1cards.dequeue()
                cardsonTable.place(1,faceDownCard1,True)
                if player1cards.size() < facedownnumber:
                   # END GAME PLAYER 2 WINs
                    cardsWar = cardsonTable.cleanTable()
                    for item in cardsWar:
                        player2cards.enqueue(item)
                    while not player1cards.isEmpty():
                        player2cards.enqueue(player1cards.dequeue())
                    print("Player 1 does not have enough cards")
                    print("Player 2 takes all cards on table and Player 1 cards")
                    endGame = True
                else:
                   # END GAME PLAYER 1 WINs
                    faceDownCard2 = player2cards.dequeue()
                    cardsonTable.place(2,faceDownCard2,True)
                    if player2cards.size() < facedownnumber:
                        cardsWar = cardsonTable.cleanTable()
                        for item in cardsWar:
                            player1cards.enqueue(item)
                        while not player2cards.isEmpty():
                            player1cards.enqueue(player2cards.dequeue())
                        print("Player 2 does not have enough cards")
                        print("Player 1 takes all cards on table and Player 2 cards")
                        endGame = True
            print(60*"-")
            pressEnter = input('')
            if player1cards.isEmpty() or player2cards.isEmpty():
                endGame = True
        winner = ""
        if player1cards.size() > player2cards.size():
            winner = "Player 1 Won"
        else:
            winner = "Player 2 Won"
        print(winner)
        print("Player 1: " + str(player1cards.size()) + " Player 2: " + str(player2cards.size()))
main()