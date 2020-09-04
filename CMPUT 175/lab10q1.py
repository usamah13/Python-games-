#Question 2

def isEven(n):
        if(n == 0): 
                return True
        elif (n == 1) :
                return False
        else:
                return isEven(n - 2)

def main():
        n = int(input("enter a number:"))
        print("is", n, "even?",isEven(n))
main()