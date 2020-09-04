#Fizz Buzz game 

def play_fb(number):
    i= 0
    while i < number:
        i = i + 1
        if i%3 ==0 and i%5 ==0:
            print(str(i)+ ' FizzBuzz')        
        elif i%3 == 0:
            print(str(i)+' Fizz')
        elif i%5 == 0:
            print(str(i) + ' Buzz')
        
        else:
            print(i)

def main():
    number =int(input('Enter maximum number to start counting >'))
    play_fb(number)
main()