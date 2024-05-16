#Text Wrap


import textwrap

def wrap(string, max_width):
    resultwrap = textwrap.wrap(string, max_width)
    s = "\n".join(resultwrap)
    return s
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
