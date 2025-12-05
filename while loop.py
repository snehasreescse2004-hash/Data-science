print("=== HCL Technologies Login System ===")

while True:   # Loop will repeat unlimited times
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == "java" and password == "123":
        print("Login successful! Welcome to Java Department.")
        break

    elif username == "python" and password == "456":
        print("Login successful! Welcome to Python Department.")
        break

    elif username == "cloud" and password == "789":
        print("Login successful! Welcome to Cloud Computing Department.")
        break

    else:
        print("Incorrect username or password. Try again...\n")

