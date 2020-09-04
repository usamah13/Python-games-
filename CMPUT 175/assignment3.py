# War Game 

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
    # TASK 1 Reading and Validating cards
    # Three Conditions
    # File Exists - raises Exception if it does not.
    # 1.Exactly 52 2.Not repeated 3.Correct Format Raises Exception if any of the 
    # above is not correct.
    # TODO
    pass


def distribute_cards(cards):
    # Task 2 Distributing cards
    # Creates Two circular Queues and return them
    # - cards is a list of valid cards that has been read from the file
    # TODO
    pass

def get_user_input():
    # Task 3 Asking user for input
    # prompt the user to enter the number of cards that would be facedown for war
    # will repeatedly ask the user to enter a valid value if any number other than 1 or 2 or 3
    # is entered
    # returns the number entered by the user
    # TODO
    pass

def compare_cards(card1,card2):
    # Task 4 Comparing Cards
    # compares card1 of player 1 with card2 of player2
    # if card1 has higher rank return 1
    # if card2 has higher rank return 2
    # if card1 is equal to card2 reurn 0
    # - card 1 is a string representing a card of player1
    # - card 2 is a string representing a card of player2
    # TODO
    pass

class onTable:
    # Task 5  Create a class to represent the table
    # an instance of this class represents the table
    def __init__(self):
        # self is the onTable object
        # TODO
        pass
    
    def place(self,player,card,hidden):
        # places the given card on the table
        # -self is the onTable object
        # -player is an object of type int. It is 1 for player1 or 2 for player 2
        # -card is an object of type str. It is the card being placed on the table
        # -hidden is an object of type bool. False when the card is faceup and True when facedown
        # TODO
        pass
    def cleanTable(self):
        # cleans the table by initializing the instance attributes
        # -self is the onTable object
        # TODO
        pass
    def __str__(self):
        # returns the representation of the cards on the table
        # -self is the onTable object
        # TODO
        pass


def main():
    # TODO - IMPLEMENT ALGORITHM HERE
    pass


main()
    