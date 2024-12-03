width = int(input("Enter the width of the rectangle: "))
height = int(input("Enter the height of the rectangle: "))
num = 0
for i in range(height):
    for j in range(width):
        print(num % 10, end=" ")
        num = num+1
    print()
