#itertools.combinations()


# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
s = input().split()
sorted_s = sorted(s[0])
for i in range(1, int(s[1])+1):
    for pair in combinations(sorted_s, i):
        print("".join(pair))
