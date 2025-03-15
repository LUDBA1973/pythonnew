cart={}

def add():
    try:
        item_name=input("Enter item name:")
        quantity=int(input("Enter quantity:"))

        if not item_name.replace(" ","").isalpha():
           raise ValueError("Item Name must contain only letters")
        
        if quantity < 0:
           raise ValueError("Quantity must be graeter than zero.")
        
    except ValueError as e:
       print(f"Error:{e}")

    else:
          cart[item_name] = quantity
          print(f"{item_name} Added. current inventory{cart}")
             
def remove():
    if cart=={}: 
        print("Cart is empty.")
        return

    try:
        item_name = input("Enter item name: ").strip()
        quantity = int(input("Enter quantity to remove: "))

        if not item_name.replace(" ", "").isalpha():
            raise ValueError("Item name must contain only letters.")

        if item_name not in cart:
            raise ValueError("Item not found in cart.")

        if quantity < 0:
            raise ValueError("Quantity must be in positive integer.")

        if quantity >= cart[item_name]:  
            raise ValueError("Quantity is greater than the available item quantity")
       

    except ValueError as e:
        print(f"Error: {e}")

    else:
            cart[item_name] -= quantity
            print(f"{quantity} {item_name}(s) removed. Current inventory: {cart}")


        
while True:
    print("1.Add 2.remove 3.exit")
    user_input= input("Enter Your Choice(1,2,3):")
    if user_input == "3":
     print(f"Exiting.... final Inventory:{cart}")
     break
    elif user_input=="1":
       add()
    elif user_input=="2":
       remove()
    else:
       print("Invalid Choice")
    
    
