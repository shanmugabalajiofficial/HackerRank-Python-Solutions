#itertools.permutations()


# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
S, size = input().split()
size = int(size)
for perm in sorted(permutations(S, size)):
    print(''.join(perm))
