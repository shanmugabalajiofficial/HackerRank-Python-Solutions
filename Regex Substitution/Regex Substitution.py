#Regex Substitution


# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

def switch(match):
    if match.group(0) == "&&":
        return ("and")
    if match.group(0) == "||":
        return ("or")

for i in range(int(input())):
    print(re.sub(r"(?<= )&&(?= )|(?<= )\|\|(?= )", switch, input()))
