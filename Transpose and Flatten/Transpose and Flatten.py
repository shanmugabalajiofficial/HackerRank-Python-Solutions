#Transpose and Flatten


import numpy

m, n = [int(num) for num in input().split(" ")]
arr = numpy.array([[int(num) for num in input().split(" ")] for _ in range(m)])
print(arr.transpose())
print(arr.flatten())
