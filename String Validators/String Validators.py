#String Validators


if __name__ == '__main__':
    s = input()

a = any(char.isalnum()for char in s)
b = any(char.isalpha()for char in s)
c = any(char.isdigit()for char in s)
d = any(char.islower()for char in s)
e = any(char.isupper()for char in s)

print(a)
print(b)
print(c)
print(d)
print(e)
