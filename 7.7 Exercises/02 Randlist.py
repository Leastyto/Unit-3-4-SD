from random import randint as rand
randList = []
for i in range(20):
    randList.append(rand(1,100))
print(randList)
print(sum(randList)/len(randList))
randList = sorted(randList)
print(randList[1],randList[-2])
evens = [x for x in randList if x % 2 == 0]
print(len(evens))