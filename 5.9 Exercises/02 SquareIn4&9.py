from math import sqrt 
amount = int(sqrt(100))
count = 0
countx = 0
for i in range (amount):
    if ((i+1)**2) %10 == 4:
        count += 1
        print ((i+1)**2)
    elif ((i+1)**2) %10 == 9:
        countx += 1
        print ((i+1)**2)

print (count, "end in 4")
print (countx, "end in 9")
