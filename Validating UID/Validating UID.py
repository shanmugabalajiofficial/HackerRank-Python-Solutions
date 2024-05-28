#Validating UID


# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

def validate_UID(UID):
    checks = [
        len(re.findall(r'[A-Z]', UID)) >= 2,
        len(re.findall(r'[0-9]', UID)) >= 3,
        bool(re.match(r'^[a-zA-Z0-9]{10}$', UID)),
        not bool(re.findall(r'(?<=(.)).*\1', UID))
    ]
    return all(checks)

for _ in range(int(input())):
    if validate_UID(input()):
        print("Valid")
    else:
        print("Invalid")
