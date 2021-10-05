def getPassword():
    while True:
        password = input("Enter a password: ")
        if len(password) < 8:
            print("Password must be at least 8 characters long.")
        elif not any(char.isdigit() for char in password):
            print("Password must contain at least one number.")
        elif not any(char.isupper() for char in password):
            print("Password must contain at least one uppercase letter.")
        elif not any(char.islower() for char in password):
            print("Password must contain at least one lowercase letter.")
        else:
            return password


pwd = getPassword()
print(f"The password is: {pwd}")
