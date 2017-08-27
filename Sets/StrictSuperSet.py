s = set(raw_input().split())
n = input()
count = 0
for i in range(n):
    s1 = set(raw_input().split())
    if not ( s1.issubset(s)):
        count = 1
if(count == 0):
    print 'True'
else:
    print 'False'
    
