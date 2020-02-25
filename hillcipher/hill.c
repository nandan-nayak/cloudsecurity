#include<stdio.h>
#include<string.h>


void main()
{
	unsigned int a[3][3]={{6,24,1},{13,16,10},{20,17,15}};
	unsigned int b[3][3]={{8,5,10},{21,8,21},{21,12,8}};
	int i,j,t=0,count=0;
	
	unsigned int c[20],d[20];
	char msg[20];

	printf("\nenter plain text : ");
	scanf("%s",msg);

	for(i=0;i<strlen(msg);i++)
	{
		c[i]=msg[i]-65;
		printf("%d",c[i]);
	
	}


	while(count*3<=strlen(msg))
	{

	for(i=0;i<3;i++)
	{
		t=0;
		for(j=0;j<3;j++)
		{
			t=t+(a[i][j]*c[(count*3)+j]);
		}	
		d[(count*3)+i]=t%26;


	}
	count++;

}
	
	printf("\n encrypted text is : ");
	for(i=0;i<strlen(msg);i++)
	{

		printf("%c",d[i]+65);

	
	}

count=0;

while(count*3<=strlen(msg))
	{
	for(i=0;i<3;i++)
	{
		t=0;
		for(j=0;j<3;j++)
		{
			t=t+(b[i][j]*d[(count*3)+j]);
		}

		c[(count*3)+i]=t%26;	

	}
count++;



}
	printf("\n decrypted text : ");
	for(i=0;i<strlen(msg);i++)
	{
		printf("%c",c[i]+65);

	}


printf("\n");

}
