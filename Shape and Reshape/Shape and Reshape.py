#Shape and Reshape


import numpy as np

data = list(map(int, input().split()))
data = np.array(data, int)
print(np.reshape(data, (3, 3)))
