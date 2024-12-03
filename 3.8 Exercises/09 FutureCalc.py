hour = int(input("Enter hour: "))
phour = int(input("How many hours ahead?: "))
print("New hour:", (hour+phour) % 12, "o'clock")