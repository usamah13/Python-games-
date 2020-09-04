#Implement the stack of ADT
# first implementation of the stack
# left end of the list as the top the stack
class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.item.insert(0,item)
    def pop(self):
        seld.items.pop(0)
    def peek(self):
        return self.items[0]
    def size(self):
        return len(self.items)
    def isEmpty(self):
        if returnlen(self.items) == 0:
            return True
        else:
            return False
    def show(self):
        print(self.items)
    def __repr__(self):
        return str(self.tems)