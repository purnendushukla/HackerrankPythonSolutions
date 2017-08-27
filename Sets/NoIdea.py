#Iteration 3 Solution :

n, m = raw_input().split()

sc_ar = raw_input().split()

A = set(raw_input().split())
B = set(raw_input().split())
print sum([(i in A) - (i in B) for i in sc_ar])

#Iteration 2 Solution :

#raw_input()
#l1 = raw_input().split()
#a = raw_input().split()
#b = raw_input().split()
#print sum( (i in a) - (i in b) for i in l1 )

# Time Out : Problem because the list a and b carry non-unique elements, Set should have been used

#Iteration 1 Solution :

#raw_input()
#l1 = raw_input().split()
#a = raw_input().split()
#b = raw_input().split()
#happy = 0
#for i in l1:
#    if(i in a):
#       happy+=1
#    elif(i in b):
#        happy-=1
#
#print happy

# Result 
# Time Out , here also the problem was a and b was not a set. Letting them as sets solve the problem.



