#include<stdio.h>
#include<string.h>
#include<ctype.h>


void main()
{

char plain[10],cipher[10];
int key,i,length;
printf("\nenter the plain text ");
scanf("%s",plain);
printf("\n enter the key ");
scanf("%d",&key);

printf("\nplain text is :%s",plain);

printf("\n encryption is \n");

for(i=0,length=strlen(plain);i<length;i++)
{
	cipher[i]=plain[i]+key;
	if(isupper(plain[i]) && (cipher[i]>'Z'))
	{
		cipher[i]=cipher[i]-26;

	}

	else if(islower(plain[i]) && (cipher[i]>'z'))
	{
		cipher[i]=cipher[i]-26;


	}
printf("\n%c",cipher[i]);


}



printf("\n Decryption is \n");

for(i=0;i<length;i++)
{
	plain[i]=cipher[i]-key;
	if(isupper(cipher[i]) && (plain[i]<'A'))
	{
		plain[i]=plain[i]+26;

	}

	else if(islower(cipher[i]) && (plain[i]>'z'))
	{
		plain[i]=plain[i]-26;


	}
printf("\n%c",plain[i]);


}





}