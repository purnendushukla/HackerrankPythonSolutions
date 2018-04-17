import numpy as np
n, m = map(int, raw_input().split())
a, b = (np.array([map(int, raw_input().split()) for _ in range(n)], dtype=int) for _ in range(2))
print a+b
print a-b
print a*b
print a//b
print a%b
print a**b

