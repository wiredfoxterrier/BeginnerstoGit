//Write a C program to find frequency of each digit in a given integer.
#include <stdio.h>
int main()
{
	int arr[10];
	int n,temp;
	printf("Enter number %d \n");
	scanf("%d",&n);
	temp = n;
	for (int i = 0;i<10;i++)
	{
		arr[i] = 0;
	}
	while(temp>0)
	{
		switch(temp%10)
		{
			case 0:arr[0]++;
			break;
			case 1:arr[1]++;
			break;
			case 2:arr[2]++;
			break;
			case 3:arr[3]++;
			break;
			case 4:arr[4]++;
			break;
			case 5:arr[5]++;
			break;
			case 6:arr[6]++;
			break;
			case 7:arr[7]++;
			break;
			case 8:arr[8]++;
			break;
			case 9:arr[9]++;
			break;
		}
		temp/=10;
	}
	for (int i = 0;i<10;i++)
	{
		printf("%d appears %d \n",i,arr[i]);
	}
}