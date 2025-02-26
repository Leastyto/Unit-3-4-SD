from math import sqrt 
amount = int(sqrt(100))
count = 0
for i in range (amount):
    if ((i+1)**2) %10 == 1:
        count += 1
        print ((i+1)**2)
print(count)



