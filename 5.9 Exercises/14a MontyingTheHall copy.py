import random
win = 0
playedGames = 0
# print("before pop:", doors)

# un comment for game stats
# print ("after pop:",doors)
# print("guess:", guess)
# print ("possible remove options:", lmontyRemove)
# print("after guess:", switchGuess)
# print("won?:", win)
switchSwitch = False
switchSwitch = input("Does the sim always switch? y/n : ").lower().strip() == "y"
if switchSwitch:
    print("Switcher initialised")
else:
    print("Sim wont switch")
recurrance = int(input("How many times should the game be simulated?: "))
for i in range(recurrance):
    doors = [0, 1, 2]
    doors[random.randint(0,2)] = 99
    guess = random.randint(0,2)
    guessElmt = doors[guess]
    winIndex = doors.index(99)
    lmontyRemove = []
    switchGuess = 0

    for i in range(len(doors)): #checks valid options to remove a door (not the car and not the guess)
        if i != winIndex and i !=guess:
            lmontyRemove.append(i)
    imontyRemove = random.choice(lmontyRemove)
    doors.pop(imontyRemove)

    guessIndex = doors.index(guessElmt) #switching doors
    if switchSwitch:
        if guessIndex == 1:
            switchGuess = 0
        elif guessIndex == 0:
            switchGuess = 1
    else:
        if guessIndex == 1:
            switchGuess = 1
        elif guessIndex == 0:
            switchGuess = 0
        
    if doors[switchGuess] == 99: #win counter
        playedGames += 1
        win += 1
    else:
        playedGames += 1

print("Sim won",win,"times.")
print("Sim played", playedGames,"times.")
print("Sim had win percentage of ", (win/playedGames)*100,"%", sep= '' )