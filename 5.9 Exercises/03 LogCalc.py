from math import log
value = int(input("Enter a value: "))
compute = 0
for i in range(value):
    compute += (1/(i+1))
print(compute - log(value)) 