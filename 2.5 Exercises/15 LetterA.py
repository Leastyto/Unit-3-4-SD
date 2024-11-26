height = int(input("How tall should the A be?: "))
remainder = height % 2
coolerheight = height - remainder
if remainder == 0:
    print("Has to be odd. Try again.")
    exit()
print(" " * coolerheight, "*", sep='')
for i in range(int((coolerheight/2)-1)):
    print(" " * (coolerheight - (i+1)), "*", " " * (2*i + 1), "*", sep='')
print(" " * int(coolerheight/2), "*" * height, sep='')
for i in range(int(coolerheight/2)):
    print(" " * int(coolerheight/2 - (i+1)), "*", " " * (height + 2 * i), "*" ,sep='')

#this took so long for no reason...