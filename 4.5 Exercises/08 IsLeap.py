year = int(input("Enter a year: "))
if year % 4 == 0:
    if year % 100 == 0 and year % 400 != 0:
        print('Not Leap')
    else:
        print("Leap")
else: 
    print("Leap")
    