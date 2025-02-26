from random import randint as rand
score = 0
cpuGuess = 0
guess = 0
for i in range(5):
    cpuGuess = rand(1,10)
    guess = int(input("Guess the number between 1 and 10: "))
    if guess == cpuGuess:
        score += 10
        print("You guessed right! Your score is now ", score, ".", sep='')
    else:
        score -= 1
        print("You guessed wrong! Your score is now ", score, ".", sep='')