#Linear Algebra


import numpy as np

N = int(input())
a = np.array([[x for x in input().split()] for i in range(N)], dtype='float')

print(round(np.linalg.det(a), 2))
