with open(r"C:\Users\Lochana\Desktop\Unit-3-4-SD\7.7 Exercises\Sample.txt","r") as file:
    lateLines = [x for x in file if " " in x]
    file.seek(0)
    inpLines = [x for x in file if " " not in x]
    file.seek(0)
splitLines = []
for x in range(len(lateLines)):
    splitLines.append(lateLines[x].split(" "))
    splitLines[x][1] = splitLines[x][1].strip("\n")
diction = {

}


for i in range(len(splitLines)):
    diction.update({int(splitLines[i][0]):int(splitLines[i][1])})


print(lateLines)
print(inpLines)
print(splitLines)
print(diction)
with open(r"output.txt", "w") as f:
    for i in range(len(inpLines)):
        f.write(str(diction[int(splitLines[i][0])]))
        f.write("\n")
