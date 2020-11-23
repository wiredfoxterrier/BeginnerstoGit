''' To reverse the 1D list given as input 
1. without using predefined function
2. using predefined function
 '''
import os 
import numpy as np 

class reversearray:
	def part1(arr):
		n = len(arr)
		b = [0]*n
		for i in range (0,len(arr)):
			b[n-i-1] += arr[i]
		print("Intial Array :",arr)
		print("New Array :",b)

	def part2(arr):
		arr = np.array(arr)
		print("Intial Array: ", arr)
		arr = np.flip(arr)
		print("New array :",arr)


	arr = list(map(int,input("\n Enter the elements: ").strip().split()))[:]
	
	part1(arr)
	part2(arr)

