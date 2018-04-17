import numpy

dim = map(int, raw_input().strip().split(' '))
print numpy.eye(dim[0], dim[1], k = 0)

# k > 0 will move the 1's diagonal along the column
# k < 0 will move the 1's diagonal along the rows
# Also, numpy.identity(3) #3 is for  dimension 3 X 3
