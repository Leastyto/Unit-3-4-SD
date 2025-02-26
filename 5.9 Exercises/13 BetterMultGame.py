from random import randint as rand
for i in range(10):
    x = rand(1, 15)
    y = rand(1, 15)
    print("Question ",(i+1),": ", x, " x ", y, " = ",sep='', end='')
    ans = int(input())
    score = 0
    if x*y == ans:
        print("Great job anklebiter, you can at least do something useful.")
        score += 1
    else:
        print("ERRRRRRRRR WRONG")
        score -= 1
if score >= 5:
    print("You scored majority correct")
if score < 5:
    print("You suck")