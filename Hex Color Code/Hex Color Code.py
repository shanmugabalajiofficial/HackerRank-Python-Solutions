#Hex Color Code


# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

pattern = r'(?<=\W)(#[a-fA-F0-9]{3}|#[a-fA-F0-9]{6})(?=\W)'
for _ in range(int(input())):
    for colour in re.findall(pattern, input()):
        print(colour)
