#Mean, Var, and Std


import numpy as np

N, M = list(map(int, input().split()))
arr = np.array([[int(x) for x in input().split()] for i in range(N)])
print(np.mean(arr, axis=1))
print(np.var(arr, axis=0))
print(round(np.std(arr, axis=None), 11))
