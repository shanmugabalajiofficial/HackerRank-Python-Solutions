#Check Strict Superset


# Enter your code here. Read input from STDIN. Print output to STDOUT
A=set(int(x) for x in input().split())
n=int(input())
t=False
c=0
for i in range(n):
    a=set(int(x) for x in input().split())
    if A.issuperset(a):
        t=True
    else:
        t=False
        c+=1
if c==0:
    print(True)
else:
    print(False)
