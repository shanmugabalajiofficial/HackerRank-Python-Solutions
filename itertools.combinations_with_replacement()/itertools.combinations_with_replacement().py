#itertools.combinations_with_replacement()


# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
s = input().split()
sorted_s = sorted(s[0])
for pair in combinations_with_replacement(sorted_s, int(s[1])):
    print("".join(pair))
