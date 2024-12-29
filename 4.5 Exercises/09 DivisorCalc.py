div =  int(input("Enter a number (if it is big this will take a while): "))
for i in range(div):
    if div % (i+1) == 0:
        print(i+1)
