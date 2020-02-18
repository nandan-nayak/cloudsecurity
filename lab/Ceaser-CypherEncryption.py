#import pyperclip
key =2
num = 0
message = "THIS IS MY SECRET MESSAGE"
mode = 'encrypt'
LETTERS='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
translated=''

for symbol in message:
    if symbol in LETTERS:
        if mode is 'encrypt':
            num=num+key
            print(num)
        elif mode is 'decrypt':
            num=num-key
    if num>=len(LETTERS):
        num=num-len(LETTERS)
        translated = translated + LETTERS[num]
    elif num<=len(LETTERS):
        #num=num+len(LETTERS)
        translated=translated+LETTERS[num]
    else:
        translated=translated+symbol
#pyperclip.copy(translated)
#print(pyperclip.paste())
print(translated)
