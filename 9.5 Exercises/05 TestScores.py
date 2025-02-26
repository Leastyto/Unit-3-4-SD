score = 0
scores = []
while score >= 0:
    score = int(input("Enter a test score: "))
    scores.append(score)
scores.pop(-1)
aGradeWorkCount = len([score for score in scores if score >= 90])
print(aGradeWorkCount)
print(sum(scores)/len(scores))