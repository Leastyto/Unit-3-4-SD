import random
i = 0
zeroList = [[0,0,0,0,0], 
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0]] 
while i < 10:
    guess = random.randint(0,4)
    guess2 = random.randint(0,4)
    if zeroList[guess][guess2] == 0:
        zeroList[guess][guess2] = 10
        i += 1
print(zeroList)