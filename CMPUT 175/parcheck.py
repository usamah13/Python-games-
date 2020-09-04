from Stack import Stack
#an example of abstraction

def parcheck(symbolString):
    index = 0
    aStack = Stack()
    balanced = True
    open_brackets = ['(','[','{']
    while index < len(symbolString) and balanced:
        if symbolString[index] in open_brackets:
            aStack.push(symbolString)
        else:
            if not aStack.isEmpty():
                balanced = False
            else:
                top = aStack.pop()
                result = match(top, symbolString[index])
                if result == False:
                    balanced = False
        index = index +1
    if aStack.isEmpty() and balanced:
        return True
    else:
        return False
def match(open_symbol,close_symbol):
    open_brackets ='({['
    close_brackets = ')}]'
    if open_brackets.index(open_symbol) == close_brackets.index(close_symbol):
        return True
    else:
        return False
def main():
    expression = input('enter expression >')
    print(parcheck(expression))
main()
    