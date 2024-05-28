#Standardize Mobile Number Using Decorators


def wrapper(f):
    def fun(l):
        # One liner => any(print(i) for i in sorted(map(lambda x: "+91 "+x[-10:-5]+" "+x[-5:], l)))
        wrapped = sorted(map(lambda x: "+91 "+x[-10:-5]+" "+x[-5:], l))
        for number in wrapped:
            print(number)
    return fun
@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
