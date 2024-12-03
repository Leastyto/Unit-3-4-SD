changen = int(input("Change amount under a dollar (in pennies): "))

if format == "D":
    changen = (changen * 100)
elif format == "P":
    changen = changen

quarter = changen // 25
changen = changen % 25
dime = changen // 10
changen = changen % 10
nickel = changen // 5
changen = changen % 5
penny = changen

print(quarter, "quarters,", dime, "dimes,", nickel, "nickels,", penny, "pennies" )