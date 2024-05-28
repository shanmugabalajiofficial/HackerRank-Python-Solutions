#The Captain's Room


# Enter your code here. Read input from STDIN. Print output to STDOUT
k=int(input())
a=list(map(int, input().split()))
b=set(a)
for i in b:
    a.remove(i)
    if i not in a:
        print(i)
        break
