bulk = int(input("How many items are you buying: "))
if bulk < 10: 
    print("$", 12*bulk, sep='')
if bulk >= 10 and bulk <= 99:
    print("$", 10*bulk, sep='')
if bulk >= 100: 
    print("$", 7*bulk, sep='')
