import numpy

A = numpy.array([raw_input().split() for _ in range(int(raw_input().split()[0]))], float)
# print option will accept formatted answer from numpy 1.13 in this case.
numpy.set_printoptions(legacy='1.13')
print numpy.mean(A, axis = 1)
print numpy.var(A, axis = 0)
print numpy.std(A, axis = None)
