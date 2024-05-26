#Company Logo


#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
    ss = set(s)
    ee = [[elem, s.count(elem)] for elem in ss]
    ff = [*sorted(ee, key=lambda x: [x[1], -ord(x[0])], reverse=True)]
for i in range(3):
    print(*ff[i])
