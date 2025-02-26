import random
money = 100
coin = False
while money <= 200 ^ money >= 0:
    coin = random.getrandbits(1) == 1
    print(coin)
    guess = input("Guess the side (h/t): ").lower().strip() == 'h'
    if guess:
        print("Heads selected!")
    else: 
        print("Tails selected!")
    if guess == coin:
        print("Guessed right!")
        money += 9
    else:
        print("Guessed wrong...")
        money -= 10
    print(money)

    