hour = int(input("Enter hour: "))
phour = int(input("How many hours ahead?: "))
ans = (hour+phour) % 12
if (hour+phour) % 12 == 0:
    ans = 12
print("New hour:", ans, "o'clock")