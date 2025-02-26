count = 0
for i in range(1, 1001):
    if not (round(i**(1/2),5) % 1 == 0 or round(i**(1/3),5) % 1 == 0 or round(i**(1/5),5) % 1 == 0): #finding the cube root is the same as x^1/3
        count += 1
print (count)