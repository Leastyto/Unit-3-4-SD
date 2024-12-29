temp = float(input("Input a temperature in degrees Celsius: "))
if temp < -273.15:
    print("Invalid temp: below absolute zero")
elif temp == -273.15:
    print("Temp is absolute zero")
elif temp < 0 and temp > -273.15 :
    print("Temp is below the freezing point of water") 
elif temp == 0:
    print("Temp is at freezing point of water")
elif temp > 0 and temp < 100:
    print("Temp is within normal range")
elif temp == 100: 
    print("Temp is at boiling point of water")
elif temp > 100: 
    print("Temp is above boiling point of water")