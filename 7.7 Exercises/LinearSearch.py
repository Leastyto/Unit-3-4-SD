from random import randint as rand
randList = []
for i in range(20):
    randList.append(rand(1,100))
print(randList)

def LinearSearch(arr, key):
    for index, element in enumerate(arr):
        if element == key:
            return(index)
    else:
        return -1
key = int(input("Enter: "))
result = LinearSearch(randList, key)
if result != -1:
    print("at", result)
else:
    print("null")