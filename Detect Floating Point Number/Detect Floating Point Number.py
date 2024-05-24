#Detect Floating Point Number


# Enter your code here. Read input from STDIN. Print output to STDOUT
for _ in range(int(input())):
    N = input()
    try:
        print(bool(float(N)))
    except ValueError:
        print(False)
