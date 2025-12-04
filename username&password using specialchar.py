username = input("enter username:")
password = input("enter password:")

special_chars = "@#$%^&*()_-+{}[]|:;<>.,?/"

if username =="admin":
    if any(char in special_chars for char in password):
        print("login successful!")
    else:
        print("password must contain at least one special character .")
else:
    print("invalid password")
        

