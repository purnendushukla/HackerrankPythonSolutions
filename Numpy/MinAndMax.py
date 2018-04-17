import numpy

print numpy.max(numpy.min(
    numpy.array([raw_input().split() for _ in range(int(raw_input().split()[0]))], int)
    , axis = 1))
