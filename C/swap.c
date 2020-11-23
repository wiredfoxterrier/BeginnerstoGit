#include <stdio.h>
int main()
{
    int a;int b;  int t;
    printf("Enter a \n"); scanf("%d",&a);
    printf("Enter b \n");scanf("%d",&b);
    t=a;
    a=b;
    b=t;
    printf("a= %d \n b= %d \n",a,b); //Using third variable
    printf("Enter a \n"); scanf("%d",&a);
    printf("Enter b \n");scanf("%d",&b);
    a = a+b;
    b = a-b;
    a = a-b;
    printf("a= %d \n b= %d \n",a,b); //Using only two variables
    return 0;
}
