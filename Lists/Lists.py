#Lists


if __name__ == '__main__':
    N = int(input())
    lst = []
    for i in range(0, N):
        x = input().split()
        if x[0] == 'insert':
            lst.insert(int(x[1]), int(x[2]))
        if x[0] == 'print':
            print(lst)
        if x[0] == 'remove':
            lst.remove(int(x[1]))
        if x[0] == 'append':
            lst.append(int(x[1]))
        if x[0] == 'sort':
            lst.sort()
        if x[0] == 'pop':
            lst.pop(-1)
        if x[0] == 'reverse':
            lst.reverse()
