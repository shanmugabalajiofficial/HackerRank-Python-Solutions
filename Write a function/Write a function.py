#Write a function


def is_leap(year):
    leap = False
    
    # Write your logic here
    if not year % 400 or (year % 100 and not year % 4):
        leap = True
    return leap

year = int(input())
print(is_leap(year))
