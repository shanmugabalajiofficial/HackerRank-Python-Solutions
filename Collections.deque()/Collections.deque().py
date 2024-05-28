#Collections.deque()


# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import deque

q = deque()

for i in range(int(input())):
    
    command = input().split()
    
    if command[0] == "append":
        q.append(int(command[1]))
    elif command[0] == "appendleft":
        q.appendleft(int(command[1]))
    elif command[0] == "pop":
        q.pop()
    elif command[0] == "popleft":
        q.popleft()
        
for i in q:
    print(i, end=" ")
