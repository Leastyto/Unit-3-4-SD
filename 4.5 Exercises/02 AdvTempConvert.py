temp = float(input("Enter a temperature : "))
format = str(input("Is that in K, C, F?: "))
endmat = str(input("Output temperature in K, C, or F?: "))
if format.capitalize is "K" and endmat.capitalize is "C":
    print(temp-273.15, "°C", sep='')
