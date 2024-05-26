#Word Order


# Enter your code here. Read input from STDIN. Print output to STDOUT
import collections

n = int(input())
word_list = collections.Counter([input() for _ in range(n)])

print(len(word_list.keys()))
print(*word_list.values())
