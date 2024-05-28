#Dot and Cross


import numpy as np

N = int(input())
a = np.array([[int(x) for x in input().split()] for i in range(N)])
b = np.array([[int(x) for x in input().split()] for i in range(N)])

print(np.dot(a, b))
