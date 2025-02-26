from random import randint as rand
randList = []
for i in range(20):
    randList.append(rand(1,100))
randList = sorted(randList)
def BinarySearch(low, high, arr, targ):
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == targ:
            return mid
        elif arr[mid] > targ:
            return BinarySearch(low, mid-1, arr, targ)
        elif arr[mid] < targ:
            return BinarySearch(mid+1, high,arr, targ)
    else:
        return -1
    
print(randList)
key = int(input("Enter: "))
result = BinarySearch(0, len(randList)-1, randList, key)
if result != -1:
    print("at", result)
else:
    print("null")