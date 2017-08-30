# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement as cwr

w = raw_input().split()
l = list(cwr(sorted(w[0]),int(w[1])))
for  i in l:
    print "".join(i)    

