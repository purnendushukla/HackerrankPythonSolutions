import numpy

N = int(input())
A = numpy.array([raw_input().split() for _ in range(N)], int)
B = numpy.array([raw_input().split() for _ in range(N)], int)

print numpy.dot(A, B)
