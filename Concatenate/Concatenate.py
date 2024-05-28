#Concatenate


import numpy as np

n, m, p = map(int, input().split())

N = np.array([list(map(int, input().split())) for _ in range(n)])
M = np.array([list(map(int, input().split())) for _ in range(m)])

print(np.concatenate((N, M)))
