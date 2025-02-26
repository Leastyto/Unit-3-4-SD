from random import randint as rand
cpuAns = rand(1,100)
userGuess = 0
attempts = 5
while userGuess != cpuAns:
    userGuess = int(input("Guess a number: "))
    if userGuess > cpuAns:
        attempts -= 1
        print("Lower! ", end='')
        if attempts == 1:
            print(attempts, "guess left.")
        else:
            print(attempts, "guesses left.")
    elif userGuess < cpuAns:
        attempts -= 1
        print("Higher! ", end='')
        if attempts == 1:
            print(attempts, "guess left.")
        else:
            print(attempts, "guesses left.")
    else:
        break
    if attempts == 0:
        print("You lose!")
        exit()
print("You win!")

