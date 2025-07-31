#List 
#grocery list

grocery_list = []

while True:
    print("\n1. Add Item\n2. Remove Item\n3. View List\n4. Search Item\n5. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        item = input("Enter item to add: ")
        grocery_list.append(item)
    elif choice == 2:
        item = input("Enter item to remove: ")
        if item in grocery_list:
            grocery_list.remove(item)
        else:
            print("Item not found!")
    elif choice == 3:
        print("Grocery List:", grocery_list)
    elif choice == 4:
        item = input("Enter item to search: ")
        if item in grocery_list:
            print("Item found!")
        else:
            print("Item not in the list.")
    elif choice == 5:
        break
    else:
        print("Invalid choice!")
