import numpy

N = input()
A = numpy.array([raw_input().split() for _ in range(N)], float)
print numpy.linalg.det(A)

