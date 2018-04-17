import numpy

inp = raw_input().strip().split(' ')
inp = map(int, inp)
arr = numpy.array(inp)
arr.shape = (3,3)
# shaping is required instead of reshaping as per ques. i.e. convert to 3x3 array
result  = arr

print arr
    
