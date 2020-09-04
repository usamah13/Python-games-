def encipher(message,key):
    # Step 1 Get the order
    sorted_key_list = sorted(key)
    order = []
    for letter in key:
        position = sorted_key_list.index(letter)
        sorted_key_list[position]='#'
        order.append(position)
    print(order)
    # Step 2 The length of the message should be multiple of length of order
    print(len(message))
    i = 0
    while (len(message) % len(order) != 0):
        message = message + ' '
    print(len(message))
    # Step 3 Create the snips
    snips = []
    i=0
    while(i<len(message)):
        snip = message[i:i+len(order)]
        snips.append(snip)
        i=i+len(order)
    print(snips)
    
    # Create the cipher
    cipher = ''
    for i in range(len(order)): # generate a sequence 0,1,2, and so on
        # find out where the number in the sequence is 
        position = order.index(i)
        for snip in snips:
            cipher = cipher+snip[position]
        cipher = cipher+'#'
    return order,cipher
        
def decipher(encoded_message,order):
    # Step 1 Remove the separator and create a list
    alist = encoded_message.split('#')
    alist.pop()
    print(alist)
    # Deciphering process
    # access the encoded message column wise - column length is length of one item in alist len(alist[0])
    # rows will be accessed as per order 3,4,5,6,0,2,1
    msg = '' 
    length = len(alist[0])
    for col_index in range(length):
        for row_index in order:
            msg = msg + alist[row_index][col_index]
    return msg
        
    
def main():
    #message = 'My brother received a new computer for his birthday. He has awesome games.'
    message = input('Enter message >')
    private_key = input('Enter key >')
    order,encoded_message = encipher(message,private_key)
    print(encoded_message)
    decoded_message = decipher(encoded_message,order)
    print(decoded_message)
    
main()
