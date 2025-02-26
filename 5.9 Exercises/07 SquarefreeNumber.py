value = int(input("Enter a number:"))
runningSum = 0
divisorList = []
isSquare = False
for check in range(1, value+1):
    if value % check == 0:
        divisorList.append(check)
        if check**0.5 % 1 == 0 and check != 1:
            isSquare = True
print(divisorList)
print(not isSquare)