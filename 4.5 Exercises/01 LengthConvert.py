
while True:
    cm = int(input("Enter a lenth in centimetres: "))
    if cm < 0: 
        print("Enter a positive number dummy. Try again.")
    else:
        print(cm,"cm in inches is ", round((cm/2.54), 2), "in.", sep="")
        break
