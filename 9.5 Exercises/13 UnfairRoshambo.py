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
pcWinRecord = 0
flag = 0
while flag == 0:
    pcchoice = rand(0,2)
    print (pcchoice)
    userchoice = input("ROCK, PAPER, or SCISSORS?: ")
    userchoice = hd[str.casefold(userchoice)]
    win = wa[userchoice][pcchoice]
    print(win)
    if win == 3:
        print("The computer chose ", hd[str(pcchoice)], ", It's a tie", sep='')
    elif win == 4:
        print("The computer chose ", hd[str(pcchoice)], ", you won", sep='')
        winrecord += 1
        print(winrecord)
    elif win == 5:
        print("The computer chose ", hd[str(pcchoice)], ", you lose", sep='')
        pcWinRecord += 1
        print(winrecord)
    if winrecord == 3:
        print("You won", winrecord, "times, you win the match!")
        flag = 1
    elif pcWinRecord == 3:
        print("You only won", winrecord, "times, you lost the match...")
        flag = 1
