# task001
x = int(input("Enter your age: "))

if 0 <= x <= 12:
    print("You are a Child")

elif 13 <= x <= 19:
    print("You are a  Teenager")

elif 20 <= x <= 59:
    print("You are a Adult")

elif x >= 60:
    print("You are a Senior citizen")

elif x < 0:
    print("Invalid age")