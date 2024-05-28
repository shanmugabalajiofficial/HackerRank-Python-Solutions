#Array Mathematics


import numpy as np

N, M = list(map(int, input().split()))
a = [[int(x) for x in input().split()] for i in range(N)]
b = [[int(x) for x in input().split()] for i in range(N)]

a = np.array(a)
b = np.array(b)

print(np.add(a, b))
print(np.subtract(a, b))
print(np.multiply(a, b))
print(np.floor_divide(a, b))
print(np.mod(a, b))
print(np.power(a, b))
