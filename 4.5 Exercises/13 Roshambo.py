from random import randint as rand
hd = {
    "rock" : 0,
    "paper" : 1,
    "scissors" : 2,
    "0" : "rock",
    "1" : "paper",
    "2" : "scissors"
}
wa = [
    [3, 5, 4],
    [4, 3, 5],
    [5, 4, 3]
]
winrecord = 0
for i in range(5):
    pcchoice = rand(0,2)
    print (pcchoice)
    userchoice = input("ROCK, PAPER, or SCISSORS?: ")
    userchoice = hd[str.casefold(userchoice)]
    win = wa[userchoice][pcchoice]
    print(win)
    if win == 3:
        print("The computer chose ", hd[str(pcchoice)], ", It's a tie", sep='')
        winrecord += 0.5
    elif win == 4:
        print("The computer chose ", hd[str(pcchoice)], ", you won", sep='')
        winrecord += 1
    elif win == 5:
        print("The computer chose ", hd[str(pcchoice)], ", you lose", sep='')
        winrecord -= 1
if winrecord >= 3:
    print("You won", winrecord, "times, you win the match!")
elif winrecord == 2.5 or winrecord == 0.5:
    print("You tied the match.")
elif winrecord <= 2:
    print("You only won", winrecord, "times, you lost the match...")
