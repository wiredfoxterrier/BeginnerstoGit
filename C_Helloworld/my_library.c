// my_library.c

#include <stdio.h>

void print_helloworld (void)
{
	printf ("Hello World\n");
}

void print_library (void)
{
	printf ("I'm a library function\n");
}

int sum_a_b (int a, int b)
{
	int ret_value = 0;

	ret_value = a + b;

	return (ret_value);
}

