from Stack import Stack
# I will be using the Satck class as a black box -----> Abstarction
def reverse(aString):
    aStack = Stack()
    for char in aString:
        aStack.push(char)
    while not aStack.isEmpty():#Very Important
        print(aStack.pop(),end = '')
def main():
    word = input('Enter word >')
    reverse(word)
main()