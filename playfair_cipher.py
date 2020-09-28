# -----------------------------------------------------------
# Creating an application which encrypts and decrypts using
# 1-D Array in playfair cipher.
#
# (C) 2020 Sandra VS Nair, Trivandrum
# email sandravsnair@gmail.com
# -----------------------------------------------------------

import math

#Initializing 
alphabet =['a','b','c','d','e','f','g','h','i','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
key_array=[]

#Creating the key as a one-dimensional array
def create_key(key):
    key=key.lower()                 #Converting to lowercase
    key=key.replace(" ", "")        #Removing whitespaces

    index=0
    flag=0
    
    for letter in key:
        if letter not in key_array:             #Insert to key array only if it is not in it already.
            if letter =='i' or letter=='j':        
                if flag == 1:
                    continue
                flag=1
                key_array[index]='i'            #Save 'i' or 'j' as 'i' itself.
                index=index+1
                continue
            
            key_array[index]=letter             #Insert to key array
            index=index+1
            
    for letter in alphabet:                     #Insert the remaining letters of the alphabet into the key array
        if letter not in key_array:
            key_array[index]=letter
            index=index+1

    print("The key is : ")
    print(key_array)

#Encrypting a message using playfair cipher
def encrypt(message):
    message=message.lower()                     #Converting to lowercase
    message=message.replace(" ", "")            #Removing whitespaces

    for i in range(0,len(message)):             #Convert all 'j' in the message to 'i'
        if message[i]=='j':
            message = message[:i] + 'i' + message[i+1:]
            
    for i in range(1,len(message),2):           #Taking pairs of letters in the message and insert bogus character 'x' in between them if they are the same.
        if message[i-1]==message[i]:
            message = message[:i] + 'x' + message[i:]

    if(len(message)%2 != 0):                    #If the length of message is an odd number, add bogus character 'x' to the end.
        length=len(message)
        message = message[:length]+'x'

    #Initializing with empty values.
    chunks = [None] * math.ceil(len(message)/2)
    encrypted_message=[None] * len(message)
    
    n = 2
    index = 0

    #Splitting the message into a list of 2-letter chunks.
    for i in range(0, len(message), n):
        chunks[index]=message[i:i+n]
        index=index+1
        
    print("The message is splitted into : ")
    print(chunks)

    index = 0
    index1 =0
    index2 = 0

    #Taking each 2-letter chunk.
    for chunk in chunks:
        first_index = 0
        second_index = 0
        first_element = 0

        #Taking first and second letter of the chunk.
        first_letter=chunk[0]
        second_letter=chunk[1]

        #Finding its index in the key array.
        index1=key_array.index(first_letter)
        index2=key_array.index(second_letter)

        #Finding the index of first element in the row of the first letter of the chunk.
        for i in range(0,21,5):
            if abs(index1-i) in range(0,5):
                first_element=i
                break

        #For letters in same column.
        if abs(index1-index2)%5 == 0:
            print('Letters in same column')
            first_index=(index1 +5)%25
            second_index=(index2 +5)%25
            encrypted_message[index] = key_array[first_index]
            index = index+1
            encrypted_message[index] = key_array[second_index]
            index=index+1
            
        #For letters in same row.
        elif index2 in range(first_element,first_element + 5):
            print('Letters in same row')
            first_index=(index1 +1)%5
            second_index=(index2 +1)%5
            encrypted_message[index] = key_array[first_index]
            index = index+1
            encrypted_message[index] = key_array[second_index]
            index=index+1
            
        #For letters not in same row/column.
        else:
            print("Letters not in same column/row")
            for i in range(first_element,first_element + 5):
                if abs(index2-i)%5 ==0:
                    first_index=i
                    break
            difference=abs(first_index - index1)
            if index1 > first_index:
                second_index=index2 + difference
            else:
                second_index=index2 - difference

            encrypted_message[index] = key_array[first_index]
            index = index+1
            encrypted_message[index] = key_array[second_index]
            index=index+1

    #Converting the list to string and printing the encrypted message.
    str1=""
    print("The encrypted message is : "+str1.join(encrypted_message)+"\n")

def decrypt(message):

    message=message.lower()                         #Converting to lowercase
    message=message.replace(" ", "")                #Removing whitespaces

    #Initializing
    chunks = [None] * math.ceil(len(message)/2)
    decrypted_message=[None] * len(message)
    n = 2
    index = 0

    #Splitting the message into a list of 2-letter chunks.
    for i in range(0, len(message), n):
        chunks[index]=message[i:i+n]
        index=index+1

    print("The message is splitted into: ")
    print(chunks)

    index = 0
    index1 =0
    index2 = 0

    #Taking each 2-letter chunk.
    for chunk in chunks:
        first_index = 0
        second_index = 0
        first_element = 0

        #Taking first and second letter of the chunk.
        first_letter=chunk[0]
        second_letter=chunk[1]

        #Finding its index in the key array.
        index1=key_array.index(first_letter)
        index2=key_array.index(second_letter)

        #Finding the index of first element in the row of the first letter of the chunk.
        for i in range(0,21,5):
            if abs(index1-i) in range(0,5):
                first_element=i
                break
        #For letters in same column.
        if abs(index1-index2)%5 == 0:
            print('Letters in same column')
            first_index=(index1 -5)%25
            second_index=(index2 -5)%25
            decrypted_message[index] = key_array[first_index]
            index = index+1
            decrypted_message[index] = key_array[second_index]
            index=index+1

        #For letters in same row.
        elif index2 in range(first_element,first_element + 5):
            print('Letters in same row')
            first_index=(index1 -1)%5
            second_index=(index2 -1)%5
            decrypted_message[index] = key_array[first_index]
            index = index+1
            decrypted_message[index] = key_array[second_index]
            index=index+1

        #For letters not in same row/column.
        else:
            for i in range(first_element,first_element + 5):
                if abs(index2-i)%5 ==0:
                    first_index=i
                    break
            difference=abs(first_index - index1)
            if index1 > first_index:
                second_index=index2 + difference
            else:
                second_index=index2 - difference

            decrypted_message[index] = key_array[first_index]
            index = index+1
            decrypted_message[index] = key_array[second_index]
            index=index+1

    #Converting the list to string and printing the decrypted message.
    str1=""
    print("The decrypted message is : "+str1.join(decrypted_message))


#Starts execution.
#Inorder to stop the program, press the key 'q'

while(True):
    key_array=[None] * 25
    choice=input('Would you like to: (1) encrypt (2) decrypt. If you want to quit, press \'q\'\n')
    if(choice == '1'):
        key=input('Please enter the key\n')
        message=input('Please enter a message to encrypt\n')
        create_key(key)
        encrypt(message)
    elif (choice == '2'):
        key=input('Please enter the key\n')
        message=input('Please enter a message to decrypt\n')
        create_key(key)
        decrypt(message)
    elif (choice == 'q'):
        break
    else:
        print('Please type either 1,2 or q')
