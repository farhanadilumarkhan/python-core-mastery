inventory = {}
while True:
    print("Inventory Management")
    print("1. Add Item")
    print("2. View Inventory")
    print("3. Update stock")
    print("4. Delete item")
    print("5. Exit")

    choice = input("Enter your choice (1 - 5)")

    if choice == '1':
        item_name = input("Item name:")
        quantity = int(input("Enter quantity:"))
        inventory[item_name] = quantity
        print(f"Item: {item_name} | Quantity: {quantity} add successfully")

    elif choice == '2':

        if not inventory:
            print("no item in inventory")

        else:
            for item, qty in inventory.items():
                print(f"Item: {item}  | Quantity: {qty}")
    
    elif choice == '3':
        item_name = input("Enter item name:")

        if item_name in inventory:
            new_qty = int(input("Update quantity"))
            inventory[item_name] = new_qty
            print(f"{item_name} : {new_qty} quantity changed")
        
        else:
            print(f"{item_name} is not in inventory") 

    elif choice == '4':
        item_name = input("Enter item name:")
        if item_name in inventory:
            del inventory[item_name] 
            print(f"{item_name} deleted succesfully")

        else:
            print(f"{item_name} does not exist")


    elif choice == '5':
        print("Program is end")
        break

    else:
        print("Invalid choice")

