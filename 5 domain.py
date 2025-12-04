# Fixed company name
company = "Tata Consultancy Services"
print(company)

# Domain-wise username and password
DS_username = "admin"
DS_password = "123@"

java_username = "admin"
java_password = "java@147"

pydevelop_username = "admin"
pydevelop_password = "pyth@123#45"

full_username = "admin"
full_password = "full@456"

uiux_username = "admin"
uiux_password = "ui@456"

# User input
domain = input("Select the domain (DS/java/pythondeveloper/fullstack/uiux): ")
username = input("Enter username: ")
password = input("Enter password: ")

# Domain checking using if-elif-else

if domain == "DS":
    if username == DS_username and password == DS_password:
        print("Login Successful - DS Department")
    else:
        print("Invalid username or password for DS!")

elif domain == "java":
    if username == java_username and password == java_password:
        print("Login Successful - Java Department")
    else:
        print("Invalid username or password for Java!")

elif domain == "pythondeveloper":
    if username == pydevelop_username and password == pydevelop_password:
        print("Login Successful - Python Developer Department")
    else:
        print("Invalid username or password for Python Developer!")

elif domain == "fullstack":
    if username == full_username and password == full_password:
        print("Login Successful - Full Stack Department")
    else:
        print("Invalid username or password for Full Stack!")

elif domain == "uiux":
    if username == uiux_username and password == uiux_password:
        print("Login Successful - UI/UX Department")
    else:
        print("Invalid username or password for UI/UX!")

else:
    print("Invalid domain!")

