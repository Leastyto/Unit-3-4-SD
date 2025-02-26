value = int(input("Enter a number:"))
runningSum = 0
for check in range(1, value+1):
    if value % check == 0:
        runningSum = runningSum+check
print(runningSum)
