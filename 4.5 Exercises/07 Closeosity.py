num1 = float(input("Input the first number: "))
num2 = float(input("Input the second number: "))
if num1 >= (num2-0.001) and num1 <= (num2+0.001):
    print("Close")
else:
    print("Not Close")