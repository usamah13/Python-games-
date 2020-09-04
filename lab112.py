def merge(left,right):
    count = 0
    result=[]
    i,j=0,0

    while i<len(left) and j<len(right):
        
        if left[i]<=right[j]: 
            result.append(left[i]) 
            i+=1
        else: 
            result.append(right[j])
            count += (len(left)-i)
            print(i)
            print(j)
            print('count is '+str(count))
            #if len(left) >1:
                #inversionbetweenlist+=1
            #else:
                #if left[i]>right[j]:
                    #inversionleft +=1                
            j+=1
    result += left[i:] 
    result += right[j:] 
    #print(inversionleft)
    #print(inversionbetweenlist)
    inversion_count = count
    print('inversion is '+str(inversion_count))
    print('result ' +str(result))
    
    return inversion_count,result

def mergeSort(data):
# Sort myself using a merge sort.
    if len(data) == 0:
        return 0, data
    if len(data) <=1: 
        return 0, data
    
    middle = len(data)//2
    #print('middle is ' +str(middle))
    inv,left = mergeSort(data[:middle])
    print('left is'+ str(left))
    inv1, right = mergeSort(data[middle:])
    print(right)
   
    inv_final, result = merge(left, right)  
    return inv1+inv_final+inv, result 
    


def main():
    alist = [10,9,8,7,6,5,4,3,2,1]
    inversion_count, sorted_list = mergeSort(alist)
    print('Inversion Count = ',inversion_count)
    print('Sorted List =',sorted_list)

main()    