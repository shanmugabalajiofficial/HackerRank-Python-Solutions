#Tuples
#Use Pypy3 for implementing this program


if __name__ == '__main__':
    n = int(input())
    tupey = tuple(int(x) for x in input().split())
    print(hash(tupey))
