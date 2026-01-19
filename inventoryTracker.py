
def show_counter(products):
    #Displays current items in the system
    print(f"\nThere are ({len(products)}) products in the system.")

def format_product_block(product):
    #Function for format of details for the product.
    name, code, qty, email, price = product
    print("-" * 28 + f" {name} " + "-" * 29)
    print(f"Code: {code}")
    print(f"Quantity: {qty}")
    print(f"Supplier: {email}")
    print(f"Price: ₱{price}")
    print("-" * 72)

def get_required_input(prompt):
    #Sends an error or warning if the fields are blank.
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input required. Please do not leave this blank.")

def add_one_product(products):
    #Function for adding one item only.
    print("\n--- Enter Product Details ---")
    name = get_required_input("Product Name: ")
    code = get_required_input("Product Code: ")
    qty = get_required_input("Quantity: ")
    email = get_required_input("Supplier Email: ")
    price = get_required_input("Unit Price: ")
    
    products.append([name, code, qty, email, price])
    print("Product added successfully!")

def add_five_products(products):
    #Loops 5 times to add 5 items, all at once; batch add.
    for i in range(1, 6):
        print(f"\nAdding Product {i} of 5:")
        add_one_product(products)

def view_all_products(products):
    #Displays all products in the list.
    if not products:
        print("\nInventory is currently empty.")
        return
    
    for item in products:
        format_product_block(item)

def search_by_code(products, query):
    #Finds the product depending on their given code 
    matches = []
    for index in range(len(products)):
        # Case-insensitive partial match
        if query.lower() in products[index][1].lower():
            matches.append(index)
    return matches

def edit_product_by_code(products):
    #Search, select, and edit a product's information.
    query = input("\nEnter Product Code (or part of it) to search for edit: ")
    match_indices = search_by_code(products, query)

    if not match_indices:
        print("No products found matching that code.")
        return

    # If multiple matches found, let the user choose
    target_index = None
    if len(match_indices) > 1:
        print("\nMultiple matches found. Select which one to edit:")
        for i, idx in enumerate(match_indices):
            print(f"[{i + 1}] {products[idx][0]} (Code: {products[idx][1]})")
        
        choice = input("Enter the number: ")
        if choice.isdigit() and 1 <= int(choice) <= len(match_indices):
            target_index = match_indices[int(choice) - 1]
        else:
            print("Invalid selection.")
            return
    else:
        target_index = match_indices[0]

    # Show current details and prompt for updates
    prod = products[target_index]
    print("\n--- Editing Product (Leave blank to keep current value) ---")
    
    new_name = input(f"New Name [{prod[0]}]: ") or prod[0]
    new_code = input(f"New Code [{prod[1]}]: ") or prod[1]
    new_qty = input(f"New Quantity [{prod[2]}]: ") or prod[2]
    new_email = input(f"New Email [{prod[3]}]: ") or prod[3]
    new_price = input(f"New Price [{prod[4]}]: ") or prod[4]

    # Update the list
    products[target_index] = [new_name, new_code, new_qty, new_email, new_price]
    print("\nUpdate Complete! New details:")
    format_product_block(products[target_index])

def main():
    # This is our main list that stores all product lists
    inventory = []

    while True:
        show_counter(inventory)
        print("\n===== INVENTORY TRACKER MENU =====")
        print("1. Add 1 Product")
        print("2. Add 5 Products")
        print("3. View All Products")
        print("4. Search Product by Code")
        print("5. Edit Product Information")
        print("0. Exit")
        
        choice = input("\nSelect an option: ")

        if choice == '1':
            add_one_product(inventory)
        elif choice == '2':
            add_five_products(inventory)
        elif choice == '3':
            view_all_products(inventory)
        elif choice == '4':
            q = input("Enter search query: ")
            results = search_by_code(inventory, q)
            if results:
                for idx in results:
                    format_product_block(inventory[idx])
            else:
                print("No results found.")
        elif choice == '5':
            edit_product_by_code(inventory)
        elif choice == '0':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

# Run the program
if __name__ == "__main__":
    main()