# Exemplar Text-1
# This is an example program.
# It contains these kinds of statements: expression, assignment,
# import, function definition.
# It contains these kinds of expressions: identifier, literal,
# attribute reference, function call, binary operator
# It uses these types:
# str, float, NoneType, function, module

import time

def main():
    name = input('What is your name?')  # get player name

    # wait
    print('Pausing...')
    time.sleep(1.5)

    print('Goodbye for now ' + name+'.')  # say goodbye by name
 
main()