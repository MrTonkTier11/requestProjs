# token: <FirstName-LastName-Last4ID>
# just edit line 1, ganyan daw kasi sabi lagay ng personal token. 

def add_item(items):
    #asks the user for the item name
    name = input("Please enter the item name: ")

    while True:
        try:
            price = float(input("Please enter the Price: ")) #will ask for the price
            break
        except ValueError:
            print("Invalid input, must be a number, try again!") #if the price input is not number, this error will show

    item = {"name":name, "price":price} #the added items and price will be added
    items.append(item) #this updates the list
    print("added successfuly!")

def view_basket(items):
    if not items: #if the items are empty
        print("Your list is empty!")
        return
    
    print("===== YOUR CURRENT BASKET =====")
    for i, item in enumerate(items, start=1): #this prints all of the current items in the list
        print(f"{i}. {item['name']} - ₱{item['price']:.2f}")

def checkout(items):
    if not items: #if the items are empty
        print("Basket is empty. Nothing to checkout.")
        return

    total = sum(item["price"] for item in items) #this calculates all of the prices of each item added

    print("\n--- Checkout ---")
    for item in items:
        print(f"{item['name']} - ₱{item['price']:.2f}")

    print(f"\nTOTAL: ₱{total:.2f}")



def main(): #main function/method of the whole program
    items = []

    while True:
        print("\n===== GROCERY BASKET+TOTAL MENU =====")
        print("1. Add Item")
        print("2. View Basket")
        print("3. Checkout")
        print("0. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            add_item(items)
        if choice == "2":
            view_basket(items)
        if choice == "3":
            checkout(items)            
        if choice == "0":
            print("EXITING PROGRAM!")
            break
        else:
            ("PLEASE ENTER AMONG THE CHOICES ONLY!")

main() #initiation
        
