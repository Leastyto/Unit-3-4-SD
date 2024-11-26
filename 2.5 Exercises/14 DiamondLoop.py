height = int(input("How tall should the diamond be?: "))
remainder = height % 2
coolerheight = height - remainder
if remainder == 0:
    print("Has to be odd. Try again.")
    exit()
for i in range(int(coolerheight/2)):
    print(" " * (int(coolerheight/2) - i), "*" * ((i*2)+1), sep='')
print("*" * height)
for i in range(int(coolerheight/2)):
    print(" " * (i+1), "*" * ((int(coolerheight/2) * 2) - (2 * i) - 1), sep='')
#who needs readability, I saved like 3 lines of code