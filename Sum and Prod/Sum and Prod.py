#Sum and Prod


import numpy as np

n, m = map(int, input().split())
arr = np.zeros(shape=[n, m], dtype=int)

for i in range(n):
    item = list(map(int, input().split()))
    arr[i] = item

print(np.prod(np.sum(arr, axis=0)))
