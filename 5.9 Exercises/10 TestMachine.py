testScores = []
for i in range(1, 11):
    print("Enter test score ",i,": ", sep='', end='')
    testScores.append(int(input()))
    if testScores[-1] > 100:
        print('\033[1m'+'\033[91m'+"Warn:"+'\033[0m'+" Score is over 100")
testScores = sorted(testScores)
print("Lowest:",testScores[0],"   Highest:",testScores[-1])
print("Average:", sum(testScores)/len(testScores))
print("Second Highest:", testScores[-2])
testScores = testScores[2:]
print("Edited Average:", sum(testScores)/len(testScores))
print(testScores)