#Set .symmetric_difference() Operation


# Enter your code here. Read input from STDIN. Print output to STDOUT
num_english = int(input())
roll_num1 = set(map(int, input().split()))
num_french = int(input())
roll_num2 = set(map(int, input().split()))

result = len(roll_num2.symmetric_difference(roll_num1))
print(result)
