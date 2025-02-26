from random import randint as rand
randList = []
for i in range(20):
    randList.append(rand(1,100))
print(randList)
def Quicksort(arr):
    if len(arr) <= 1:
        return arr
    piv = arr[0]
    lesser = [x for x in arr if x < piv]
    equal = [x for x in arr if x == piv]
    greater = [x for x in arr if x > piv]
    lesser = Quicksort(lesser)
    greater = Quicksort(greater)
    return lesser + equal + greater
print(Quicksort(randList))