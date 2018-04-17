import numpy

dim = map(int, raw_input().strip().split(' '))

array_1 = numpy.array([map(int, raw_input().strip().split(' ')) for _ in range(dim[0])], int)
array_2 = numpy.array([map(int, raw_input().strip().split(' ')) for _ in range(dim[1])], int)
print numpy.concatenate((array_1, array_2), axis = 0)
