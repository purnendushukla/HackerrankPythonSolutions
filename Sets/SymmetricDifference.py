input()
s1=set(map(int, ((raw_input().split()))))
input()
s2=set(map(int, ((raw_input().split()))))
ss = sorted(s1 ^ s2)
for i in ss:
    print(i)
