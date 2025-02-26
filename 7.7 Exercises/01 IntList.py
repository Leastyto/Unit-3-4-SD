userListInt = list(eval(input("Enter a list: ")))
print(userListInt)
print(len(userListInt))
print(userListInt[-1])
# i could use userListInt.reverse but i dont want to!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
print([userListInt[i] for i in range(len(userListInt)-1, -1, -1)])
if 5 in userListInt:
    print("yuh")
else:
    print("nuh")
# i could also use userListInt.count(5) but i also dont want to!!!
countFive = 0
ltFive = 0
for i in range(len(userListInt)):
    if userListInt[i] == 5:
        countFive += 1
    
print(countFive)
del userListInt[0]
del userListInt[-1]
# i concede, im not writing a whole sorting algorithm
print(sorted(userListInt))

for i in range(len(userListInt)):
    if userListInt[i] < 5:
        ltFive+= 1

print(ltFive)