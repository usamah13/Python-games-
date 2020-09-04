import operator

def unzip(new):

    list1=[]
    list2=[]
    if len(new) >0:
        #print(len(new))
        for i in range(len(new)):
            list1.append(new[i][0])
            list2.append(new[i][1])            
            #flattened = []
            #for sublist in new:
                #for val in sublist:
                    #flattened.append(val)  
            #sorted_list = sorted(flattened)
    
   
            #list1 = sorted_list[:len(sorted_list)//2]
            #list2 = sorted_list[len(sorted_list)//2:]
    
            
    else:
        list1 = []
        list2 = []
         
    
    final_list = [ list1, list2]
    return final_list
    
    
    
def main():
    
    #tuples = input('Enter a list of tuples ()()()')
    
    tuples_list1 = [(1,2)]
    tuples_list2 = [(1,4),(2,5),(3,6)]
    tuples_list3 = [('A','B'),('X','Y')]
    tuples_list4 = []
    #print(tuples_list)
    
    new_list1 = unzip(tuples_list1)
    print(new_list1)
    new_list2 = unzip(tuples_list2)
    print(new_list2)
    new_list3 = unzip(tuples_list3)
    print(new_list3)
    new_list4 = unzip(tuples_list4)
    print(new_list4)    
    
main()