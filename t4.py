# task004
size = input("Choose pizza size (small/medium/large): ").lower().strip()
total = 0
if size == "small":
    total = 15
elif size == "medium":
    total = 20
elif size == "large":
    total = 25
else:
    print("Invalid size selected.")
    exit()

pepper = input("Add pepper? (yes/no): ").lower().strip()
if pepper == "yes":
    if size == "small":
        total += 2
    elif size == "medium" or size == "large":
        total += 3
    # else:
    #     print("Invalid input.")
    #     exit()

cheese = input("Add extra cheese? (yes/no): ").lower().strip()
if cheese == "yes":
    total += 1
elif cheese =="no":
    total += 0
# else:
#     print("Invalid input.")
#     exit()

print(f"Your total bill is: ${total}")