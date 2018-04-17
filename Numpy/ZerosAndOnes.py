import numpy
# tuple is needed to be used
num = tuple(map(int, raw_input().strip().split(' ')))
print (numpy.zeros(num, dtype = numpy.int))
print (numpy.ones(num, dtype = numpy.int))
