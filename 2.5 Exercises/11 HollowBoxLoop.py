width = int(input("How wide should the box be?: "))
height = int(input("How tall should the box be?: "))
print("*" * width)
for i in range(int(input("How tall should the box be?: "))-2):
    print ("*", (" " * (width - 2)), "*", sep='')
print("*" * width)