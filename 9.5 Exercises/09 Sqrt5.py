guess = 1
userAsk = int(input("Enter a number to sqrt: "))
for i in range(1000):
    guess = ((guess)+(userAsk/guess))/2
print(guess)
