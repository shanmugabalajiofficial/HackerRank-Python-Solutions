#Min and Max


import numpy
N, M = list(map(int, input().split()))
mat = [[int(i) for i in input().split()] for _ in range(N)]
mat = numpy.array(mat)
mini = numpy.min(mat, axis=1)
print(numpy.max(mini))
