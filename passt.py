# Correct password
correct_password = "securepassword"

# Number of attempts allowed
max_attempts = 3

print("Welcome! You have 3 attempts to enter the correct password.")

# Loop for password attempts
for attempt in range(1, max_attempts + 1):
    user_input = input(f"Attempt {attempt}: Enter your password: ")
    print("gg",user_input)
    if user_input == correct_password:
        print("Access granted!")
        break
    else:
        remaining_attempts = max_attempts - attempt
        if remaining_attempts > 0:
            print(f"Incorrect password. You have {remaining_attempts} attempt(s) remaining.")
        else:
            print("Account locked. Too many failed attempts.")