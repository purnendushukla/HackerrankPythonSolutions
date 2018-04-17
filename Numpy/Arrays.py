import numpy 


def arrays(arr):
	return numpy.array(arr, float)[::-1]
	# with this one liner we are creating a view in this array which is reversed.
	# another solution type.
	# return numpy.flipud(numpy.array(arr, float))

arr = raw_input().strip().split(' ')
result = arrays(arr)
print(result)	
