plainlower="abcdefghijklmnopqrstuvwxyz"
plainupper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"


keylower="qwertyuiopasdfghjklzxcvbnm"
keyupper="QWERTYUIOPASDFGHJKLZXCVBNM"


cipher=""

plain=input("enter the plain text : ")
print("coresponding Encrypted text")
for i in plain:
	result=""
	if plainlower.find(i) >=0:
		index=plainlower.index(i)
		result=keylower[index];
		cipher+=result
	elif plainupper.find(i)>=0:
		index=plainupper.index(i);
		result=keyupper[index];
		cipher+=result;
	print(result);
plain=""
print("coresponding Decrypted text")
for i in cipher:
	result=""
	if keylower.find(i) >=0:
		index=keylower.index(i)
		result=plainlower[index];
		plainupper+=result
	elif keyupper.find(i)>=0:
		index=keyupper.index(i);
		result=plainupper[index];
		plain+=result;
	print(result);