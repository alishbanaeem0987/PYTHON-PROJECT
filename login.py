usernamearray = ["admin", "alishba"]
passwordarray = ["abc123", "12345"]
while True:

    print("\nWelcome to the login system!")
    print("1.login")
    print("2. register")
    print("3. exit")
    input_choice = input("Enter your choice (1-3): ")
    if input_choice == "1":
        # login section
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        error_message = "Invalid username or password. Please try again."
        if username in usernamearray:
            index = usernamearray.index(username)
            if password == passwordarray[index]:
                print("Login successful!")
                break
            else:
                print(error_message)
        else:
            print(error_message)
    elif input_choice == "2":
        # register section
        new_username = input("Enter a new username: ")
        if new_username in usernamearray:
            print("Username already exists. Please choose a different username.")
        else:
            new_password = input("Enter a new password: ")
            usernamearray.append(new_username)
            passwordarray.append(new_password)
            print("Registration successful! You can now log in.")
    elif input_choice == "3":
        print("Exiting the program. Goodbye!")
        break
    






