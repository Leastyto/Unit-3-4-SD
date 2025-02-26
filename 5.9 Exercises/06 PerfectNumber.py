def divise(value): #function to check if a number is perfect
    runningSum = 0
    for check in range(1,(value+1)):
        if value % check == 0: #if the number is divisible by the looped number, add it to the tally "runningSum"
            runningSum+=check   
    if runningSum-check == value: #numbers are only perfect if their divisors (excluding themselves) sum to their value
        print(value)
for n in range(1,10001): #call the function 10000 times (no clue how to make it more efficient)
    divise(n)
