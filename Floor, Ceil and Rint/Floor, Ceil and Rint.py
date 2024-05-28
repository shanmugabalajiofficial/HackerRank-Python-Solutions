#Floor, Ceil and Rint


import numpy as np
np.set_printoptions(legacy='1.13')

A = np.array(list(map(float, input().split())))
print(np.floor(A), np.ceil(A), np.rint(A), sep="\n")
