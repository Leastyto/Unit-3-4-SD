import random 
countryList = ["canada", "australia", "england", "wales", "scotland", "ireland", "mexico", "jamaica", "singapore", "china", "india", "colombia", "panama", "tibet", "azerbaijan"]
gameChoice = random.choice(countryList)
wordBreakdown = [letter for letter in gameChoice]
ghostWord = ["-" for letter in wordBreakdown]
# print(f"{wordBreakdown} , {ghostWord}")
print(ghostWord)
wrongAttempt = 0
while ghostWord != wordBreakdown and wrongAttempt != 5:
    playerGuess = input("Guess a letter: ").lower().strip()
    for index, value in enumerate(wordBreakdown):
        if playerGuess == value:
            ghostWord[index] = playerGuess
            print(ghostWord)
        elif playerGuess not in wordBreakdown:
            wrongAttempt += 1
            print("Wrong guess.")
            print(ghostWord)
            break
