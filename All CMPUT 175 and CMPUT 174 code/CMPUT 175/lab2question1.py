# Coin guessing game:

from random import randint

def target_value():
    return (randint(1,99))
    
def check_uservalue(userinput):
    if var.isdigit() and int(userinput) in [1,5,10,25]:
            inputValue = int(userinput)
            #goalInt -= inputValue
            #print(goalInt)
            #return goalInt
            return True
    elif userinput.strip() == '':
            #print('End')
            #return False
            quit = False 
            
    else:
        #print('Invalid entry- Try again!')
        return False
    
    
def display_end(is_win, Total_value):
    print('Game Session Ends')
    print('Here is your outcome :')
    if is_win == True:
        print ('Success!')
        play_another_game()
        
    else:
        print('Failure you entered'+str(Total_value)+'cents')
        delta(target_value())
    
    
def play_game():
        #print( target_value())
        accepeted_coins = [1,5,10,25]
        goalstr = str(target_value())
        
        print('Game Session Starts')
        print('Enter coins values as 1-penny, 5-nickel, 10-dime,and 25-quater.')
        print('Enter coins add up to '+ goalstr+',one per line')
def input_funtion():
    var = input('Enter a valid coin >')
    return var
    
def main():
    quit = false
    if not quit:
       
        play_game()
        Total_value = 0
        goalInt = (target_value())
        var = input('Enter a valid coin >')
        while goalInt!=0:
            var = input_function()
            outcome = check_uservalue(var)
            if not outcome:
                print( 'Invalid entry please try again')
                input_function()
            else:
                Total_value += var
                goalInt -=var
            
    




main()