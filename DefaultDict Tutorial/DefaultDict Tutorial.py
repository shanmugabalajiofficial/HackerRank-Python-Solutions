#DefaultDict Tutorial


# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())
        
A = [input() for i in range(1, n+1)]
B = [input() for j in range(1, m+1)]

for j in B:
    matches = []
    for index, value in enumerate(A):
        if value == j:
            matches.append(str(index+1))
            
    if matches:
        print(" ".join(matches))
    else:
        print(-1)
