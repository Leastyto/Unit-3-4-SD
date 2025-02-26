weight = int(input("Enter a weight in kilos: "))
while weight <= 0:
    print("Invalid weight.")
    weight = int(input("Enter a weight in kilos: "))
    
print(weight*2.2)