#Second assessment Vending Machine
#Printing an ASCII art banner for the Vending Machine
print("""
██╗   ██╗███████╗███╗   ██╗██████╗ ██╗███╗   ██╗ ██████╗     ███╗   ███╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗███████╗
██║   ██║██╔════╝████╗  ██║██╔══██╗██║████╗  ██║██╔════╝     ████╗ ████║██╔══██╗██╔════╝██║  ██║██║████╗  ██║██╔════╝
██║   ██║█████╗  ██╔██╗ ██║██║  ██║██║██╔██╗ ██║██║  ███╗    ██╔████╔██║███████║██║     ███████║██║██╔██╗ ██║█████╗  
╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║  ██║██║██║╚██╗██║██║   ██║    ██║╚██╔╝██║██╔══██║██║     ██╔══██║██║██║╚██╗██║██╔══╝  
 ╚████╔╝ ███████╗██║ ╚████║██████╔╝██║██║ ╚████║╚██████╔╝    ██║ ╚═╝ ██║██║  ██║╚██████╗██║  ██║██║██║ ╚████║███████╗
  ╚═══╝  ╚══════╝╚═╝  ╚═══╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝
                                                                                                                     
""")

#Items available in the vending machine, categorized into Drinks and Snacks
class VendingMachine:
    def __init__(self):
        self.items = {
            "Drinks": {
                #Defining drink items with their respective details
                1: {"name": "Coke", "price": 5.00, "quantity": 10},
                2: {"name": "Mountain Dew", "price": 5.00, "quantity": 15},
                3: {"name": "Masafi", "price": 1.00, "quantity": 10},
                4: {"name": "Starbucks Coffee", "price": 8.00, "quantity": 15},
                5: {"name": "Lipton", "price": 3.00, "quantity": 12}
            },
            "Snacks": {
                #Defining snack items with their respective details
                6: {"name": "Lays", "price": 5.00, "quantity": 20},
                7: {"name": "Cheetos", "price": 5.00, "quantity": 18},
                8: {"name": "Sneakers", "price": 3.00, "quantity": 20},
                9: {"name": "Twix", "price": 2.00, "quantity": 15},
                10: {"name": "Cookies", "price": 3.00, "quantity": 10}
            },
            "Toys": {
                #Define toy items with their respective details
                11: {"name": "Bounce Ball", "price": 5.00, "quantity": 15},
                12: {"name": "Barbie", "price": 15.00, "quantity": 10},
                13: {"name": "stuffed Toy", "price": 8.00, "quantity": 13},
                14: {"name": "Keychain", "price": 3.00, "quantity": 15},
                15: {"name": "Mini Car", "price": 10.00, "quantity": 10}
            }
        }
        #Total money inserted by the user
        self.money_inserted = 0  

    #Displaying the available items in the vending machine
    def display_items(self):
        print("Welcome to the Vending Machine!")
        print("Here are the available items:")
        for category, items in self.items.items():
            print(f"\n{category}:")
            for item_num, item_info in items.items():
                print(f"{item_num}. {item_info['name']} - ${item_info['price']}")

    #Allowing the user to select an item and manage the purchase process
    def select_item(self):
        while True:
            try:
                choice = int(input("Enter the number of the item you want to buy (or 0 to exit): "))
                if choice == 0:
                    print("Thank you for using the vending machine!")
                    break
                selected_item = None

                #Search for the selected item in the available categories
                for category, items in self.items.items():
                    if choice in items:
                        selected_item = items[choice]
                        break
                if selected_item is None:
                    print("Invalid item number. Please try again.")
                    continue
                if selected_item['quantity'] == 0:
                    print("Sorry, this item is out of stock.")
                    continue

                #Dispense the selected item and calculate change
                self.dispense_item(selected_item)
                self.calculate_change(selected_item['price'])
                break
            except ValueError:
                print("Invalid input. Please enter a valid item number.")

    #Allow the user to select an item and manage the purchase process
    def select_item(self):
        while True:
            try:
                choice = int(input("Enter the number of the item you want to buy (or 0 to exit): "))
                if choice == 0:
                    print("Thank you for using the vending machine!")
                    break
                selected_item = None

                #Search for the selected item in the available categories
                for category, items in self.items.items():
                    if choice in items:
                        selected_item = items[choice]
                        break
                if selected_item is None:
                    print("Invalid item number. Please try again.")
                    continue
                if selected_item['quantity'] == 0:
                    print("Sorry, this item is out of stock.")
                    continue

                #Dispense the selected item and calculate change
                self.dispense_item(selected_item)
                self.calculate_change(selected_item['price'])

                #Suggest complementary item if available
                suggested_item = self.get_complementary_item(choice)
                if suggested_item:
                    print(f"Would you like to try {suggested_item['name']} as well?")

                break
            except ValueError:
                print("Invalid input. Please enter a valid item number.")
    #A method to suggest complementary items based on the selected item
    def get_complementary_item(self, selected_item_number):

        #Define a dictionary of suggestions (you can modify this as needed)
        suggestions = {
            1: 6,
            2: 7,
            3: 8,
            4: 9,
            5: 10,

            6: 1,
            7: 2,
            8: 3,
            9: 4,
            10: 5,
            #Add more suggestions as needed
        }
        
        #Check if there's a suggestion for the selected item
        suggested_number = suggestions.get(selected_item_number)
        if suggested_number:
            for category, items in self.items.items():
                if suggested_number in items:
                    return items[suggested_number]
        return None
    #Calculate and manage the change for the inserted money
    def calculate_change(self, price):
        while self.money_inserted < price:
            try:
                money = float(input("Please insert money (or 0 to cancel): $"))
                if money == 0:
                    print("Transaction canceled. Returning money.")
                    return  #Stop further processing if canceled

                #Add the inserted money
                self.money_inserted += money  
                if self.money_inserted < price:
                    needed_amount = price - self.money_inserted
                    print(f"Please insert at least ${needed_amount:.2f} more to complete the payment.")
            except ValueError:
                print("Invalid input. Please enter a valid amount.")

        change = self.money_inserted - price
        print(f"Your change is ${change:.2f}. Thank you for your purchase!")
        self.money_inserted = 0
    
    #Dispense the selected item and update its quantity
    def dispense_item(self, item):
        print(f"You've selected: {item['name']} - ${item['price']}")
        item['quantity'] -= 1
        print(f"Here is your {item['name']}.")


#Example usage
def run_vending_machine():
    vending_machine = VendingMachine()
    vending_machine.display_items()
    vending_machine.select_item()

run_vending_machine()