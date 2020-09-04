class DLinkedListNode:
    # An instance of this class represent a node in Double Linked List
    def __init__(self,initData,initNext,initPrevious):
        self.data = initData
        self.next = initNext
        self.previous = initPrevious
        
        if initNext != None:
            self.next.previous = self
        if initPrevious != None:
            self.previous.next = self
    def getData(self):
        return self.data
    def setData(self,newData):
        self.data = newData
    def getNext(self):
        return self.next
    def getPrevious(self):
        return self.previous
    def setNext(self,newNext):
        self.next = newNext
    def setPrevious(self,newPrevious):
        self.previous = newPrevious
class DLinkedList:
    # An instance of this class represents the Double Linked List
    def __init__(self):
        # - self is the DLL object
        self.head = None
        self.tail = None
        self.size = 0
    def __str__(self):
        # return a string representation of DLL object
        # - self is the DLL object
        string = ''
        current = self.head
        while(current != None):
            string = string + str(current.getData()) + '<->'
            current = current.getNext()
        return string
    def add(self,item):
        # adds an item at the start of the list
        # - item is the reference to the data in the DLL node
        new_node = DLinkedListNode(item,self.head,None)
        if self.size == 0:
            self.tail = new_node
        self.head = new_node
        self.size = self.size + 1
    def append(self,item):
        # adds an item at the the end of the list
        # - item is the reference to the data in the DLL node
        pass # TO BE COMPLETED
    
    def insert(self,pos,item):
        # inserts the item at the pos
        # raises exception if pos is not an int
        # raises exception if pos < 0
        # - item is reference to the data in the DLL node
        # - pos is location where item should be inserted
        assert isinstance(pos,int),'pos has to be of type int'
        assert pos >= 0,'pos has to be greater than or equal to 0'
        # TO BE COMPLETED
        
    def pop(self): # I FIXED THIS - IT NOW RETURNS THE DATA
        # removes the node that is at end of the list and return the data
        # - self is the DLL object
        if self.size == 0:
            raise Exception('List is Empty!')
        value = self.tail.getData()
        if self.size == 1:
            self.head = None
            self.tail = None
            
        else : # more than one
            # value = self.tail.getData()
            self.tail = self.tail.getPrevious()
            self.tail.setNext(None)
        self.size = self.size - 1
        return value
    
    def remove(self,item):
        # removes the given item from the list
        # raises an exception if list is empty with message List is Empty
        # raises an exception if item not in list with message Item not in list
        # -item is reference to data in the node
        # -self is the DLL object
        if self.size == 0:
            raise Exception('List is empty !')
        found = False
        previous = None 
        current = self.head
        while current.getNext() != None and not found:
            if current.getData() == item :
                found = True
            else:
                previous = current
                current = current.getNext()
        if not found:
            raise Exception('Item not found')
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        if current.getNext() != None: # I FIXED THIS - BRACKETS () WERE MISSING
            current.getNext().setPrevious(previous)
        else:
            self.tail = previous
        self.size = self.size - 1 # I FIXED THIS - SIZE WAS NOT BEING DECREMENTED BEFORE
def main():
    # Testing Double Linked List
    dlist = DLinkedList()
    dlist.append(2)
    dlist.append(4)
    dlist.append(6)
    dlist.append(77)
    dlist.append('A')
    dlist.add('Z')
    print('List after append and add')
    print(dlist)
    print()
    dlist.insert(0,'start')
    print('After inserting the word start at position 0')
    print(dlist)
    print()
    dlist.insert(7,'end')
    print('After inserting the word end at position 7')
    print(dlist)
    print()
    dlist.insert(4,'middle')
    print('After inserting middle at position 4')
    print(dlist)
    
main()
