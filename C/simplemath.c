#include <stdio.h> 
int main() 
{
int number1;
int number2;
int rem,sum,quo,diff;
printf("Enter First Number: \t"); scanf("%d",&number1);
printf("Enter Second Number: \t"); scanf("%d",&number2);
rem = number1%number2;
sum = number1+number2;
diff = number1-number2;
quo=number1/number2;

printf("Sum of the two numbers is : %d \n",sum); 
printf("Remainder of the two numbers is : %d \n",rem); 
printf("Quotient of the two numbers is : %d \n",quo);
printf("Difference of the two numbers is : %d \n",diff);
return 0;

} 
