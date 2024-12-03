a, b = 0, 1
n = int(input("How many Fibonacci numbers to print?: "))
for i in range(n):
    if i == n-1:
        print(a)
    else:
        print (a, end=', ')
        a, b = b, a+b
