power = int(input("Enter a power: "))
HMLastDit = int(input("Enter how many digits do you wanna see?: "))
LastDit = ((2 ** power) % (10**HMLastDit))
print(LastDit)