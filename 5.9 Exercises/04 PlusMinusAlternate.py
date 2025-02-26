compute = 0
for i in range(2001):
    if i % 2 == 0:
        compute += (-i)
    else:
        compute += i
print (compute)