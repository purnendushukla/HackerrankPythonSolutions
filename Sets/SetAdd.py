n = input()
count  = 0
set1 = set()
for i in range(0,n):
    x = raw_input()
    set1.add(x)
for i in set1:
    count+=1 
print count     
