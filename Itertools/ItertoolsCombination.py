# combinations() method generates sorted combinations if input is sorted

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
w = raw_input().split()

for i in range(1,int(w[1])+1):
    l = list(combinations(sorted(w[0]),i))
    for j in l:
        print "".join(j)
 
