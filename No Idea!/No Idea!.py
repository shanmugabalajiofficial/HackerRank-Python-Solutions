#No Idea!


n_and_m = input().split()
n = n_and_m[0]
m = n_and_m[1]
arr = map(int, input().split())
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))
happiness = 0
for i in arr:
    if i in set_a:
        happiness +=1
    if i in set_b:
        happiness-=1
print(happiness)
