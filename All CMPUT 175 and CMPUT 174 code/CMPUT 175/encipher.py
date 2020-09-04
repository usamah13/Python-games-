def encipher(message,key):
    #change the clear message to cipher text
    #- message clear mssage of type str
    #- key is the private key of type str
    
    key_list = sorted(key)
    print(key_list)
    #get the order
    order = []
    for letter in key:
        position = key_list.index(letter)
        #print(position)
        key_list[position] = '' # for duplicate private keys
        order.append(position)
    print(order)
    # Make the length of the message multiple of the leghth of the order
    print(len(message))
    while len(message) % len(order) != 0:
        message = message + ' '
    print(len(message))
    #create snips
    snips = []
    i = 0
    while(i<len(message)):
        chunk = message[i:i+len(order)]
        snips.append(chunk)
        i = i + len(order)
    print(snips)
    print(i)
    # create the cipher
    cipher = ''
    for i in range(len(order)):
        column = order.index(i)
        for chunk in snips:
            cipher = cipher + chunk[column]
        cipher = cipher + '#'
    
    return cipher,order


def decipher(cipher, order):
    #something abou the function 
    #- parameter 1 
    #- parmeter 2
    cipher.split('#')
    prin(alist)
    alist.pop()
    # access the list columnwise

def main():
    
    message = 'My brother recived a new computer for his birthday. He has awesome games.'
    private_key = 'CMPT175'
    #private_key = 'ABBA'
    cipher_text,order = encipher(message, private_key)
    #clear_message = decipher(cipher_text,order)
    print(cipher_text)
    
    
main()