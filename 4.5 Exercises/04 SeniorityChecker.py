cred = int(input("How many credits have you taken?: "))
if cred <= 23: 
    print("Freshman spotted. Launching super senior.")
if cred >= 24 and cred <= 53: 
    print("Sophomore detected. Irrelevant user discarded.")
if cred >= 54 and cred <= 83:
    print("Junior identified. Initiating super senior training program.")
if cred >= 84:
    print("Welcome back senior. Go get them soldier.")