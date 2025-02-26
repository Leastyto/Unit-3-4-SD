import random
randList = ["because", "pencilcase", "bottle", "understanding", "beware", "of", "snakes", "china", "library", "novels"]
duplicate = []
for x in range(len(randList)):
    for letter in randList[x]:
        if randList[x].count(letter) > 1 and randList[x] not in duplicate:
            duplicate.append(randList[x])
print(random.choice(duplicate))