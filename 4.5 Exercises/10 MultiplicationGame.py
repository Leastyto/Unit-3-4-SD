from random import randint as rand
for i in range(10):
    x = rand(1, 15)
    y = rand(1, 15)
    print("Question ",(i+1),": ", x, " x ", y, " = ",sep='', end='')
    ans = int(input())
    if x*y == ans:
        print("Great job anklebiter, you can at least do something useful.")
    else:
        print("ERRRRRRRRR WRONG")
    