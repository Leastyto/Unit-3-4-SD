culpritList = [0, 0, 1 , 1, 1, 0, 1]
flag = 0
for num in culpritList:
    if culpritList[num] == 0 and flag == 0:
        culpritList[num] = 1
        flag = 1

print(culpritList)