#Validating Credit Card Numbers


# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
validation = r'^(?=[456])(?!.*(\d)(-?\1){3})\d{4}(-?\d{4}){3}$'
for _ in range(int(input())):
    if re.match(validation, input()):
        print("Valid")
    else:
        print("Invalid")
