#Merge the Tools!


def merge_the_tools(string, k):
    # your code goes here
    import textwrap
    l = textwrap.wrap(string,k)
    for i in range(len(l)):
        print("".join(dict.fromkeys(l[i])))
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
