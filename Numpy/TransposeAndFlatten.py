n, m = map(int, input().split())
array = numpy.array([input().strip().split() for _ in range(n)], int)

print (array.transpose())
print (array.flatten())

# simplistic approach of line 2 for understanding
# for i in range(0,dim[0]):
#     l.append(raw_input().strip().split(' '))
# arr = numpy.array(l,int)


