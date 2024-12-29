hour = int(input("Enter hour: "))
status = str.casefold(input("Is it am or pm: "))
if status == "pm":
    status = status+12
phour = int(input("How many hours ahead?: "))
div = (hour+phour)//12
rem = (hour+phour)%12
if div % 2 == 1:
    if status == "am":
        status = "pm"
    elif status == "pm":
        status = "am"
if rem == 0:
    rem = 12
print(rem, status)