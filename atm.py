balance = 5000

while balance > 0:
  
    print(f"Current balance: {balance}")
    
    withdrawal = int(input("Enter withdrawal amount: "))
    
    while withdrawal > balance:
        print("Error: Withdrawal amount exceeds balance. Try again.")
    if withdrawal <= 0:
        print("Error: Invalid withdrawal amount. Try again.")
    else:
        balance -= withdrawal
        print(f"{withdrawal} withdrawn successfully.Current balance: {balance}")
    
    if balance == 0:
        print("Balance is zero. Simulation ends.")
        break
    
    choice = input("Do you want to continue? (yes/no): ").lower()
    if choice == "no":
        print("simulation ended...")
        break