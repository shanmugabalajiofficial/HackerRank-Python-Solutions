#Iterables and Iterators


# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import comb

N = int(input())
aCount = input().count("a")
K = int(input())
probability = 1 - comb(N-aCount, K)/comb(N, K)
print(f"{probability:.3f}")
