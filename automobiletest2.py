class Automobile:
    
    # Constructor:
    def __init__(self, length, horsepower, color):
        self._length = length
        self._horsepower = horsepower
        self._color = color
        
    # Returns the length:
    def get_length(self):
        self._length = input('Enter automobile\'s length in meters :')
        return self._length
    
    # Returns the horsepower:
    def get_horsepower(self):
        self._horsepower = input('Enter automobile\'s horsepower :')
        return self._horsepower
        # TODO: You must implement this method!
    
    # Returns the color:
    def get_color(self):
        self._color = input('Enter automobile\'s color:')
        return  self._color
        # TODO: You must implement this method!
    
    #Returns the worth:
    def get_worth(self):
        color_factor = 0
        if self._color == 'red':
            color_factor = 3
        elif self._color == 'yellow' or 'blue':
            color_factor = 2
        else:
            color_factor = 1
            
        
        worth = self._horsepower*self._length*color_factor*10
        
        return worth
        # TODO: You must implement this method!
    
# Main function, which asks the user for the length, horsepower, and color of
# an automobile, and will then print out the worth of that automobile:
def main():
    #length = int(input('Enter automobile\'s length in meters: '))
    #horsepower = int(input('Enter automobile\'s horsepower: '))
    #automobile = Automobile(length, horsepower, color)
    Automobile.get_length()
    Automobile.get_horsepwer()
    Automobile.get_color()
    
    worth = Automobile.get_worth()
    
    print('This automobile is worth $'+str(worth))
    # TODO: You must implement this function!

main()