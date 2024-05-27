#Find Angle MBC


# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
AB = float(input())
BC = float(input())
# u'\xb0' is unicode degree
MBC = str(round(math.degrees(math.atan2(AB, BC))))+u'\xb0'
print(MBC)
