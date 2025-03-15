# task003

acc_balance = 1000
print("your account balance",acc_balance)
amount = int(input("Enter withdrawal amount:"))

if amount > acc_balance:
    print("Insufficient funds")
elif amount < 0:
    print("Invalid amount")
else:
    acc_balance -= amount
    #  acc_balance= acc_balance-amount
    print("Withdrawal successful.Remaining balance:", acc_balance)
 