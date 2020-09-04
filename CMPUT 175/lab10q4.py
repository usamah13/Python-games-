def reverseDisplay(number):
    if (number < 10):
        print(number, end = '')
        return number
    else:
        print(number%10, end = '')
        return reverseDisplay(int(number/10))   
def main():
    number= int(input('Enter a number :'))
    reverseDisplay(number)
main()