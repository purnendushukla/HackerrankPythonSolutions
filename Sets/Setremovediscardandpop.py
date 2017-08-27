n = int(input())

s = set(map(int, raw_input().split()))

N = int(input())

for i in range(N) :
    choice=raw_input().split()
    if choice[0]=="pop" :
        s.pop()
    elif choice[0]=="remove" :
        s.remove(int(choice[1]))
    elif choice[0]=="discard" :
        s.discard(int(choice[1]))
print sum(s)
