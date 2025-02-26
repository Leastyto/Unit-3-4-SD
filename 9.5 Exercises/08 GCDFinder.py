def GCDFinder(x,y):
    while y !=0:
        rem = x % y
        x, y = y, rem
    return(x)
y = int(input("Enter a number: "))
x = int(input("Enter another: "))
if y > x:
    y, x = x, y
print(GCDFinder(x, y))
