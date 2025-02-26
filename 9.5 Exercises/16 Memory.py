boardDisplay = [["*","*","*","*"],
                ["*","*","*","*"],
                ["*","*","*","*"],
                ["*","*","*","*"]]
boardActual = [["A","E","E","C"],
                ["H","C","B","I"],
                ["D","B","A","I"],
                ["F","D","H","F"]]
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
nums = [i for i in range(0,26)]
playerCord1 = [letter for letter in input("Enter a coordinate: ")]
print(playerCord1)
zipper = list(zip(alphabet, nums))
zipperDict = dict(zipper)
print(zipperDict[playerCord1[0]])
print(int(playerCord1[1])-1)
print(boardActual[int(playerCord1[1])-1][zipperDict[playerCord1[0]]])
playerCord2 = [letter for letter in input("Enter a coordinate: ")]
if boardActual[int(playerCord1[1])-1][zipperDict[playerCord1[0]]] == boardActual[int(playerCord2[1])-1][zipperDict[playerCord2[0]]]:
    print("dingdingdingdingdingding")