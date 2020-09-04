from BoundedQueue import BoundedQueue
from CircularQueue import CircularQueue
import time

def main():
    
    circular = CircularQueue(100000)
    bounded = BoundedQueue(100000)
    
    for i in range(100000):
        circular.enqueue(i)
        bounded.enqueue(i)
        
    start1 = time.time()
    while not circular.isEmpty():
        circular.dequeue()
    end1 = time.time()
    
    circulartime = end1 - start1
    
    start2 = time.time()
    while not bounded.isEmpty():
        bounded.dequeue()
    end2 = time.time()
    
    boundedtime = end2 - start2 
    
    
    print('For Bounded Queue, the total runtime of dequeing 100000 is:\n' + str(boundedtime))
    print('For Circular Queue, the total runtime of dequeing 100000 is:\n' + str(circulartime))
    
main()
    
        
        