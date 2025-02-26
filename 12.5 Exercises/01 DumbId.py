initRead = [line for line in open(r"C:\Users\Lochana\Desktop\Unit-3-4-SD\12.5 Exercises\01 ClassScore")]
dataRead = [line.split() for line in initRead]
print(initRead)
print(dataRead)
with open(r"C:\Users\Lochana\Desktop\Unit-3-4-SD\12.5 Exercises\01a ClassScore", "w") as file:
    for i in range(len(initRead)):
        file.write(dataRead[i][0])
        file.write(" ")
        file.write(str(int(dataRead[i][1])+5))
        file.write("\n")