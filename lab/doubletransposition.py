import numpy as np
msg = "attackxatxdawnx"
ciphertext = np.array(list(msg))
ciphertext = ciphertext.reshape(5,3)
print(ciphertext)
rowkey = list(input("enter the key in row permutation"))
columnkey = list(input("enter the key in column permutation"))
print(rowkey)
print(columnkey)
encrypttxt = np.array(list(msg)).reshape(5,3)
decrypttxt = np.array(list(msg)).reshape(5,3)
l = -1
for i in rowkey:
    l = l+1
    k = 0
    for j in columnkey:
        encrypttxt[l][k] = ciphertext[np.int(i)][np.int(j)];
        k = k+1
l = -1
for i in rowkey:
    l = l + 1
    k = 0
    for j in columnkey:
        decrypttxt[l][k] = encrypttxt[np.int(i)][np.int(j)];
        k = k + 1
print(encrypttxt)
print(decrypttxt)