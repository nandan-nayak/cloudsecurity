plain=input("enter the plain Text : ")
key=int(input("enter key : "))
cipher=""

print("corresponding Encrypted text  is ")
for  i in plain:
    
    c=ord(i)
    #print("c=",c)
    if c>=97:
        c=(c+key)%124;
        if c<27:
            c=c+97;
    elif c>=65 and c<=91:
        c=(c+key)%91;
        if c<27:
            c=c+65;
    
    o=chr(c)
    cipher+=o
    print(o)


print("corresponding Decrypted text is ")
for  i in cipher:
    
    c=ord(i)
    #print("c=",c)
    if c>=97:
        c=(c-key)%124;
        if c<27:
            c=c+97;
    elif c>=65 and c<=91:
        c=(c-key)%91;
        if c<27:
            c=c+65;
    
    o=chr(c)
    cipher+=o
    print(o)
#print(plain)
#print(key)
