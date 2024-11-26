Meal = int(input("How much $ did you pay for your meal?: "))
Tip = (Meal*((int(input("What % do you want to tip?: ")))/100))
print ("You're tipping ", Tip, "$, and your total bill is ", Meal, "$", sep='')