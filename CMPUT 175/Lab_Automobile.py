class Automobile:
    
    # Constructor:
    def __init__(self, length, horsepower, color):
        self._length = length
        self._horsepower = horsepower
        self._color = color
        
    # Returns the length:
    def get_length(self):
        
        return self._length
    
    # Returns the horsepower:
    def get_horsepower(self):
        
        return self._horsepower
        # TODO: You must implement this method!
    
    # Returns the color:
    def get_color(self):
       
        return  self._color
        # TODO: You must implement this method!
    
    #Returns the worth:
    def get_worth(self):
        color_factor = 0
        length = self.get_length()
        horsepower = self.get_horsepower()
        color = self.get_color()
        if color == 'red':
            color_factor = 3
        elif color == 'yellow' or color == 'blue':
            color_factor = 2
        else:
            color_factor = 1
            
        worth = horsepower*length*color_factor*10
        
        return worth
        # TODO: You must implement this method!
    
# Main function, which asks the user for the length, horsepower, and color of
# an automobile, and will then print out the worth of that automobile:
def main():
    length = int(input('Enter automobile\'s length in meters: '))
    horsepower = int(input('Enter automobile\'s horsepower: '))
    color = input('Enter automobile\'s color: ')
    automobile = Automobile(length, horsepower, color)
    worth = automobile.get_worth()
    
    print('This automobile is worth $'+str(worth))
    # TODO: You must implement this function!

main()
