 
def merge(left,right):
    result=[]
    i,j=0,0
    inversionleft= 0
    inversionright = 0 
    inversionbetweenlist = 0
    global count
    #x=0
    #y=0
    #while x <len(left)-1:
        #if left[i]>=left[i+1]:
            #inversionleft +=1
        #x+=1
    #while y <len(left)-1:
        #if right[i]>=right[i+1]:
            #inversionright +=1  
        #y+=1

    while i<len(left) and j<len(right):
        
        if left[i]<=right[j]: 
            result.append(left[i]) 
            i+=1
        else: 
            result.append(right[j])
            count += (len(left)-i)
            print(i)
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
def length(alist):
    return len(alist)
count =0
def mergeSort(data):
# Sort myself using a merge sort.
    if len(data) ==0:
        return 0, data
    x = length(data)
    if len(data) <=1: 
        return data
    middle = len(data)//2
    #print('middle is ' +str(middle))
    #print(mergeSort(data[:middle])
    left = mergeSort(data[:middle])
    print('left is'+ str(left))
    right = mergeSort(data[middle:])
    print(right)
   
    #if len(left[:])>1 or (len(right[:])>1):
    if isinstance(left, tuple) and isinstance(right, tuple):
        #count += merge(count,left[1],right[1])[0]
        #if count <0:
            #count =0
        #('count' +str(count))
        return merge(left[1],right[1])
    
    elif isinstance(right,tuple):
        #count += merge(left,right[1])[0]
        #if count <0:
            #count =0        
        return merge(left,right[1])
    
    elif isinstance(left, tuple):
        #count += merge(count,left[1],right)[0]
        #if count <0:
            #count =0        
        return merge(left[1],right)
    
    else:
        #count += merge(count,left,right)[0]
        #if count <0:
            #count =0        
        return merge(left,right)


def main():
    alist = [10,9,8,7,6,5,4,3,2,1]
    inversion_count, sorted_list = mergeSort(alist)
    print('Inversion Count = ',inversion_count)
    print('Sorted List =',sorted_list)

main()    