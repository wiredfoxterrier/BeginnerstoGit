// Write a C program to swap first and last digits of a number.
#include <stdio.h>
int main()
{
	int n;
	int fd,ld,rev;
	printf("Enter Number \n");
	scanf("%d",&n);
	int temp = n;
	ld = n%10;
	rev = 0;
	while(temp>0)
	{
		fd=temp%10;
		rev = rev*10+fd;
		temp= temp/10;
		
	}
	int newnum = ld;
	temp = rev/10;
	while(temp>9)
	{
		newnum = newnum*10+(temp%10);
		temp/=10;
	}
	newnum = fd+(newnum*10);
	printf("The reverse number is %d",newnum);
	return 0;

}
