from itertools import product

A = map(int, raw_input().split())
B = map(int, raw_input().split())
X = list(product(A,B))
for i in X:
    print i, 
    
    
