#Validating phone numbers


# Enter your code here. Read input from STDIN. Print output to STDOUT

def checkMobileNo(mobileNo):
    try:
        if len(mobileNo)==10 and mobileNo.startswith(('7', '8', '9')):
            if int(mobileNo):
                return 'YES'
    except Exception:
        return 'NO'
    return 'NO'
    
for i in range(int(input())):
    mobileNo = input()
    print(checkMobileNo(mobileNo))
