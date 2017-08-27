from __future__ import division


def average(l):
    # your code goes here
    s = set(l)
    sum = 0
    count = 0
    for i in s: 
        sum +=i
        count+=1
    avg = sum/count
    return avg
   
# No need to be chenged.

l = []
n = input()
for i in range(0,n):
	x = input()
	l.append(x)
	
print average(l)	
	
   
