while True:
    angle = int(input("Enter an angle between -180◦ and 180◦: ")) 
    if angle > 180: 
        print("Has to be 180 or below. Try again.")
    elif angle < -180:
        print("Has to be -180 or above. Try again.")
    else: 
        break
print(angle, "◦ is equivalent to ", angle+180, end='◦.', sep='')