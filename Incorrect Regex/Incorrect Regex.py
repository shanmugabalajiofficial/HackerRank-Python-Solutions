#Incorrect Regex
#Use Pypy3 for implementation

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n = int(input())

for _ in range(n):
    strings = input()
    try:
        print(bool(re.compile(strings)))
    except re.error:
        print('False')
