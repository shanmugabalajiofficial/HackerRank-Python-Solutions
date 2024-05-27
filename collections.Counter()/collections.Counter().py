#collections.Counter()


#Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
X = input()
shoe_sizes = input()
N = input()
money_earned =0
shoe_sizes = [int(n) for n in (shoe_sizes.split())]
# print(Counter(shoe_sizes))
for row in range(0, int(N)):
    desired = [int(n) for n in ((input()).split())]
    # print(row,desired)
    
    if int(desired[0]) in Counter(shoe_sizes).keys():
        money_earned += int(desired[1])
        shoe_sizes.remove(int(desired[0]))
    
print(money_earned)
