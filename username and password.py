correct_username ="sneha"
correct_password ="123"

entered_username = input("enter your username:")
entered_password = input("enter your password:")

if entered_username == correct_username and entered_password == correct_password:
    print("login successful! welcome.")
else:
    print("invalid username or password.please try again.")

