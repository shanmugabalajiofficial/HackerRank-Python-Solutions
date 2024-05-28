#Validating and Parsing Email Addresses


# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
import email.utils

for _ in range(int(input())):
    name, address = input().split()
    if bool(re.match(r'^[a-zA-Z][-\w.]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$', email.utils.parseaddr(address)[1])):
        print(name, address)
