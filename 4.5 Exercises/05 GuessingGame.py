from random import randint as rand
num = rand(1, 10)
x = int(input("Guess a number between 1 and 10: "))
if x == num: 
    print("wow man you got it right...mhm....yea")
if x != num:
    print("you IMBECILE.", x, "is nowhere NEAR", num, end='.')