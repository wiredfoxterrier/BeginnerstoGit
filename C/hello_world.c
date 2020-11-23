#include "my_library.h"
#include <stdio.h>


int main (void)
{
	int i = 10, j = 20;
	int result = 0;

	printf ("I'm in main function\n");
	
	print_helloworld ();

	print_library ();

	result = sum_a_b (i, j);

	printf ("result = %d\n", result);
}