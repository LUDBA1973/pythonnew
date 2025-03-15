inventory = {}

def add_item(item, quantity):
    if quantity <= 0:
        print("Error: Quantity must be a positive integer.")
        return
    inventory[item] = inventory.get(item, 0) + quantity
    print(f"Added {quantity} of {item}. Current stock: {inventory[item]}")

def remove_item(item, quantity):
    if item not in inventory:
        print("Error: Item not found in inventory.")
        return
    if quantity > inventory[item]:
        print("Error: Cannot remove more than available stock.")
        return
    inventory[item] -= quantity
    if inventory[item] == 0:
        del inventory[item]
    print(f"Removed {quantity} of {item}. Current stock: {inventory.get(item, 0)}")

def display_inventory():
    print("Current Inventory:")
    for item,qty in inventory.items():
        print(f"{item}: {qty}")
    if not inventory:
        print("Inventory is empty.")

def main():
    while True:
        action = input("Enter operation (add, remove, exit): ").strip().lower()
        if action == "exit":
            print("Exiting...")
            break
        elif action in ("add", "remove"):
            item = input("Enter item name: ").strip()
            try:
                quantity = int(input("Enter quantity: ").strip())
                if action == "add":
                    add_item(item, quantity)
                else:
                    remove_item(item, quantity)
            except ValueError:
                print("Error: Quantity must be an integer.")
        else:
            print("Invalid operation. Please enter 'add', 'remove', or 'exit'.")
        

main()