# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
x = raw_input().split()
perm = list(permutations(x[0],int(x[1])))
perm.sort()
for i in perm:
    print "".join(i)
