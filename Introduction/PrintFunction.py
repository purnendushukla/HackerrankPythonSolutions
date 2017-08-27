from __future__ import print_function
print(*range(1,input()+1),sep='')

# Print Function defines the input as *objects not like iterable objects

#print instead needs multiple arguments for each object you want to print. * is a way to "unpack" a list so that it becomes arguments instead of a list. *[1,2,3] converts to (1,2,3). Example using print (from future in py2): print([1,2,3])
