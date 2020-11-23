'''
Find the minimum and maximum 
1.without using external functions 
2. using external functions
'''
class minmax:
	def part1(arr):
		large = -99999999999999
		small = 99999999999999
		for i in range(0,len(arr)):
			if(small>arr[i]):
				small = arr[i]
			if(large<arr[i]):
				large = arr[i]
		print("Max :",large,"\n Min :",small)

	def part2(arr):
		print("Max :",max(arr),"\n Min :",min(arr))


	arr = list(map(int,input("\n Enter the elements: ").strip().split()))[:]

	part1(arr)
	part2(arr)


