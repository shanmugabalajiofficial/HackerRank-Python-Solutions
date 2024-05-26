#Find the Runner-Up Score!


if __name__ == '__main__':
    n = int(input())
    arr =list(map(int, input().split()))
    arr.sort()
    x = max(arr)
    i = arr.index(x)
    print(arr[i-1])
