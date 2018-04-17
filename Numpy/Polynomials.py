import numpy

A = numpy.array(raw_input().split(), float)
B = input()
print numpy.polyval(A, B)

