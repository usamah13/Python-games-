def sumdigits(num):
    sum=0
    if (num == 0):
        return sum
    else:
        sum = (num%10 )+ sumdigits(int(num/10));
        return sum    

def main():
    number=int(input('Enter a number:'))
    print(sumdigits(number))
main()