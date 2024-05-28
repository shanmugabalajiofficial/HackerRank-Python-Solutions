#Symmetric Difference


# Enter your code here. Read input from STDIN. Print output to STDOUT
M = input()
a = set(map(int, input().split()))
N = input()
b = set(map(int, input().split()))
print(*sorted(b^ a), sep='\n')
