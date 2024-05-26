#Input()


# Enter your code here. Read input from STDIN. Print output to STDOUT
x, k = map(int, input().split())
polynomial = input()
expression = polynomial.replace('x', str(x))
result = eval(expression)

if result == k:
    print(True)
else:
    print(False)
