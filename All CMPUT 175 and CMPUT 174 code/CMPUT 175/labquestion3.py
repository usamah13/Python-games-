# Counting the number of itegers entered 
def count_numbers(astring):
    # Convert a string to a list
    count = {} # an empty dictionary
    alist = astring.split()
    #print(alist)
    
    # iterate over the numbers in the list
    for number in alist:
        if number in count: # inside the dictionary - update the value
            count[number] = count[number] +1
        else:# not in the dictionary yet
            count[number] = 1
    print(count)
    #for key in count.keys():
        #print( key +' occurs '+str(count[key])+' times')
    for k,v in count.items():
        if v != 1:
            print(k+' occurs '+ str(v) +' times')
        else:
            print(k+' occurs one time')
        
        
def main():
    integers = input('Enter numbers seperated by spaces :')
    count_numbers(integers)
main()
