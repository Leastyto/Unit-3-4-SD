temp = float(input("Enter a temperature : "))
format = str(input("Is that in K, C, F?: "))
endmat = str(input("Output temperature in K, C, or F?: "))
if str.capitalize(format) == "K" and str.capitalize(endmat) == "C":
    print(round(temp-273.15, 3), "°C", sep='')
elif str.capitalize(format) == "K" and str.capitalize(endmat) == "F":
    print(round((temp-273.15)*(9/5)+32, 3), "°F", sep='')
elif str.capitalize(format) == "K" and str.capitalize(endmat) == "K":
    print(temp, "K", sep='')
elif str.capitalize(format) == "C" and str.capitalize(endmat) == "K":
    print(round(temp+273.15, 3), "K", sep='')
elif str.capitalize(format) == "C" and str.capitalize(endmat) == "F":
    print(round(temp*(9/5)+32, 3), "°F", sep='')
elif str.capitalize(format) == "C" and str.capitalize(endmat) == "C":
    print(temp, "°C", sep='')   
elif str.capitalize(format) == "F" and str.capitalize(endmat) == "C":
    print(round((temp-32)*(5/9),3))
elif str.capitalize(format) == "F" and str.capitalize(endmat) == "K":
    print(round(((temp-32)*(5/9)+273.15), 3))
elif str.capitalize(format) == "F" and str.capitalize(endmat) == "F":
    print(temp, "°F", sep='')   