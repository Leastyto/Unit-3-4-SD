userStr = input("Enter a string: ")
userChar = (input("Enter a search char: "))
finder = userStr.find(userChar) 
if finder == -1:
    print("No instance found.")
else:
    print(userChar, "found at index", finder)