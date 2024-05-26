#Collections.OrderedDict()


# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
N = input()
value = 0
od = OrderedDict()
for row in range(0, int(N)):
    kargs = input().split()
    item_name = " ".join(kargs[:-1])
    net_price = int(kargs[-1])
    value = od.get(item_name, 0)
    od[item_name] = net_price +value
    
for key, value in od.items():
    print(key, value)
