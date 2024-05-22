#Set .add()


# Enter your code here. Read input from STDIN. Print output to STDOUT
a=int(input())
variableset=set()
for i in range(a):
    variableset.add(input())
    count=(len(variableset))
print(count)
