plain=input("enter the plain Text : ")
key=int(input("enter key : "))
cipher=""
#encrypttext=""
def encrypt(plain):
    global cipher
    print("corresponding Encrypted text  is ")
    for  i in plain:
        
        c=ord(i)
    
        #print("c=",c)
        if c>=97:
            c=(c+key)%123;
            if c<27:
                
                c=c+97;
                #print("c<27",chr(c))
        elif c>=65 and c<=91:
            c=(c+key)%91;
            if c<27:
                c=c+65;
        
        o=chr(c)
        cipher+=o
    print(cipher)
        



    
def decrypt(message):
    LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for key in range(len(LETTERS)):
        translated = ""
        for symbol in message:
            if symbol in LETTERS:
                num = LETTERS.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(LETTERS)
                translated = translated + LETTERS[num]
            else:
                translated = translated + symbol
        print("Decryption using Key #%s: %s" % (key, translated))   
              
              
              
encrypt(plain)

decrypt(cipher.upper())



'''
print("corresponding Decrypted text is ")
for  i in cipher:
    
    c=ord(i)
    #print("c=",c)
    if c>=97:
        #c=(c-key)%124;
        c=c+(26-key)
        if c>=123:
            c=(c-123)+97
        
    elif c>=65 and c<=91:
        c=c+(26-key)
        if c>=91:
            c=(c-91)+65;
    
    o=chr(c)
    cipher+=o
    print(o)
#print(plain)
#print(key)
'''    
    
    
    
    
    
    
    
    
    
'''

              
decrypt()

'''