password = input("Enter password: ")
correctPass = "password123"
attempts = 0
while password != correctPass:
    print("Wrong!")
    attempts += 1
    password = input("Enter password: ")
    if attempts == 4:
        print("Locked out!")
        exit()
print("Logged in!")