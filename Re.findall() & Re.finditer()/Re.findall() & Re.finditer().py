#Re.findall() & Re.finditer()


# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
import string

vowels = "aeiouAEIOU"
consonants = "".join(x for x in string.ascii_letters if x not in vowels)
pattern = r'(?<=[%s])[%s]{2,}(?=[%s])' % (consonants, vowels, consonants)
vowels = re.findall(pattern, input())
if vowels:
    for match in vowels:
        print(match)
else:
    print(-1)
