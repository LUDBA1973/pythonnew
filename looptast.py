pswd = "abdul"
attempt=1

while attempt <= 3:
        user_input = input(f"Attempt {attempt}: Enter your password: ")
        if pswd == user_input:
                print("Access granted!")
                break
        else:
             remaining_attempts = 3-attempt
        if remaining_attempts > 0:
            print(f"Incorrect password. You have {remaining_attempts} attempt(s) remaining.")
            print("Wrong Password:",user_input)
        else:
            print("Account locked. Too many failed attempts.")
            print("Wrong Password:",user_input)

        attempt+=1