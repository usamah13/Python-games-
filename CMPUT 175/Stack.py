# Second Implementation of Stack Class
# This uses the right side of the list as the top of the Stack

class Stack:
    def __init__(self):
        self.items =[] # instance attribute/property
    def push(self,item): # mutator, setter
        self.items.append(item) # is now O(1) instead of O(n)
    def pop(self): # mutator,setter
        return self.items.pop() # is now O(1) instead of O(n)
    def peek(self):# accessor,getter
        return self.items[len(self.items)-1] # returns the item at the last index instead of first
    def isEmpty(self):
        return self.items == []
    def show(self):
        print(self.items)
    def size(self):
        return len(self.items)
