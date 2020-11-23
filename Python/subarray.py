K = 3
A = [1,2,1,3,4]
ctr = 0 
uniqueint = 0
subarray = []
for i in range(0,len(A)):
	for j in range(0,len(A)):
		if A[j] in subarray:
			if uniqueint == K:
				ctr+= 1
			    subarray.append(A[j])
			    print("",subarray)
		    else:
			    subarray.append(A[j])

	    elif uniqueint < K:
		    subarray.append(A[j])
		    uniqueint+= 1
	    else:
		    ctr+= 1
		    print("",subarray)
		    subarray = [] 
		    uniqueint = 0
		    break



print("",ctr)
