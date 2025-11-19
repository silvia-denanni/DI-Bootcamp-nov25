# Daily Challenge day 4 :Coffee Shop Menu Manager
# The KEY is the drink name (string)
# The VALUE is the price (float)

menu = {
    "espresso": 7.0,
    "latte": 12.0,
    "cappuccino": 10.0
}

def show_menu(menu_dict):    #"""Print all drinks and prices."""
    if not menu_dict:  # NOT checks if the dictionary is empty
        print("The menu is empty")
    else:
        for drink, price in menu_dict.items(): #it loops through each key/value (drink, price) and prints them formatted
            print(f"{drink} - {price}₪")

#show_menu(menu)
pass

def add_item(menu_dict):
    #"""Add a new drink to the menu."""
    user_drink = input("Please enter a drink name: ")
    drink_price = float(input("Please enter a drink price: "))
    if drink_price < 0:
        print("invalid price")
        return

    if user_drink in menu_dict:
        print(f"Drink {user_drink} already exists!")   
    else: 
        menu[user_drink] = drink_price
        print(f"{user_drink} added to the menu")
#add_item(menu)         
pass

def update_price(menu_dict):
    #"""Change the price of an existing drink."""
    user_drink_new = input("Please enter the drink name you want to update: ")

    if user_drink_new in menu_dict:
        drink_price_new = float(input("Please enter the new drink price: "))
        if drink_price_new < 0:
            print("invalid price")
            return

        menu[user_drink_new] = drink_price_new     #we are updating the price of the drink AFTER we know it is already there
        print("Price updated!")        
    else: 
        print("Item not found!")

#update_price(menu)   
pass


def delete_item(menu_dict):
#     """Remove a drink from the menu."""
    user_drink_delete = input("Please enter the drink name you want to remove: ")
    if user_drink_delete in menu_dict:
        del menu[user_drink_delete]
        print("Drink deleted.")
    else:
        print("Drink not found.")

#delete_item(menu)
pass

def search_item(menu_dict):
    drink_search = input("Search a drink name: ")
    if drink_search in menu_dict:
        print("The price is: ", menu[drink_search])    # [drink_search] is returning the value of the key inside the menu, the "+" concatenates it to the string before
    else:
        print("Not in the menu.")
pass    

def show_options():
#     """Print the available actions."""
    print("What  would you like to do?\n 1. Show menu\n 2. Add item\n 3. Update price\n 4. Delete item\n 5. Search\n 6. Exit")
#show_options()
pass

def run_coffee_shop():
    while True: 
        show_options()
        user_choice = int(input(""))
        if user_choice == 1:
            show_menu(menu)
        elif user_choice == 2:
            add_item(menu)
        elif user_choice == 3:
            update_price(menu)
        elif user_choice == 4:
            delete_item(menu)
        elif user_choice == 5:
            search_item(menu)
        elif user_choice == 6:
            print("Goodbye!")
            break                #this breaks the loop from going on 
        else:
            print("Invalid choice, try again.")
pass
# Start the program
run_coffee_shop()