# a Python program that asks the user to enter a full name in the following 
#format :LastName, FirstName MiddleName

import re
def  main():
    
    input_string = 'Enter name [Last name, FirstName MiddleName]>'
    
    name = input(input_string)
    
    name_list = re.split(',|\s',name)
    name_list.remove('')
    print(name_list)
    
    name_string = 'The new name is:'
    
    print(name_string +'<{0:^10}><{1:>5}>.<{2:<10}>'.format(name_list[1],name_list[2][0],name_list[0]))
    
main()
    