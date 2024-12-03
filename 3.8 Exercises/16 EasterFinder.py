year = int(input("Year: "))
cent = (year // 100)
m = (15 + cent - ((cent / 4) // 1) - (((8 * cent + 13)/25) // 1)) % 30
n = (4 + cent - ((cent / 4) // 1)) % 7
a = (year % 4)
b = (year % 7)
c = (year % 19)
d = (19 * c + m) % 30
e = (2 * a + 4 * b + 6 *d + n) % 7
posmarch = int(22 + d + e)
posapril = int(d+e-9)
if d == 29 and e == 6:
    posapril = 19
elif d == 28 and e == 6 and m in [2, 5, 10, 13, 16, 21, 24, 39]:
    posapril = 18
if  0 < posapril < 30:
    print("In ", year, ", Easter falls on April ", posapril, end='.', sep='')
elif 0 < posmarch < 31:
    print("In ", year, ", Easter falls on March ", posmarch, end='.', sep= '')
# painstakingly checked if the output is correct :c
