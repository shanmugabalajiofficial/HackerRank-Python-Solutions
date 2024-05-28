#Any or All


# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
nums = list(map(int, input().split()))

if all(num > 0 for num in nums) and len(nums) == n:
    p = [num for num in nums if str(num) == str(num)[::-1]]
    if p:
        print(True)
    else:
        print(False)
else:
    print(False)
