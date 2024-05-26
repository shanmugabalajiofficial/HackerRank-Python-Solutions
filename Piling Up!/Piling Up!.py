#Piling Up!


for _ in range(int(input())):
    len_cube=input()
    cube_lst=list(map(int, input().split()))
    if max(cube_lst) != cube_lst[len(cube_lst)-1] and max(cube_lst) != cube_lst[0]:
        print('No')
    elif max(cube_lst) == set(cube_lst):
        print('Yes')
    else:
        print('Yes')
