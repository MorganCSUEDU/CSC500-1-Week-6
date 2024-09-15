# week 4
grocery_items = [
    ("Apples", 0.50, "Fresh red apples"),
    ("Bananas", 0.30, "Ripe yellow bananas"),
    ("Bread", 2.00, "Whole wheat bread loaf"),
    ("Milk", 2.50, "1 gallon of whole milk"),
    ("Eggs", 3.00, "A dozen large eggs"),
    ("Cheese", 4.00, "Sharp cheddar cheese block"),
    ("Cereal", 3.50, "Whole grain cereal box"),
    ("Pasta", 1.50, "Dry spaghetti pasta"),
    ("Tomatoes", 1.00, "Fresh vine tomatoes"),
    ("Onions", 0.75, "Yellow onions"),
    ("Potatoes", 1.25, "Russet potatoes"),
    ("Chicken", 5.00, "Boneless chicken breast"),
    ("Beef", 6.00, "Ground beef"),
    ("Fish", 7.00, "Fresh salmon fillet"),
    ("Rice", 2.00, "Long-grain white rice"),
    ("Beans", 1.00, "Canned black beans"),
    ("Carrots", 0.75, "Fresh carrots"),
    ("Lettuce", 1.50, "Crisp romaine lettuce"),
    ("Yogurt", 2.00, "Greek yogurt"),
    ("Ice Cream", 4.50, "Vanilla ice cream"),
    ("Coffee", 5.00, "Ground coffee"),
    ("Tea", 3.00, "Herbal tea"),
    ("Juice", 2.50, "Orange juice"),
    ("Soda", 1.50, "Carbonated soft drink"),
    ("Chips", 2.00, "Potato chips"),
    ("Cookies", 2.50, "Chocolate chip cookies"),
    ("Candy", 1.00, "Mixed candy pack"),
    ("Chocolate", 2.00, "Dark chocolate bar"),
    ("Soap", 1.50, "Bar of soap"),
    ("Shampoo", 3.50, "Bottle of shampoo")
]

TAX_RATE = 0.09
BAG_COST = 0.08
ITEMS_PER_BAG = 5

# ItemToPurchase class definition
class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        total = self.item_price * self.item_quantity
        print(f"{self.item_name}: {self.item_quantity} @ ${self.item_price:.2f} = ${total:.2f}")

def print_store_menu():
    print("\n" + "="*40)
    print("Welcome to the Simple Grocery Store!")
    print("="*40)
    for i, (item, price, description) in enumerate(grocery_items, 1):
        print(f"{i:2}. {item:<15} ${price:.2f}")
        if i % 6 == 0:
            print()

def get_user_selection():
    while True:
        try:
            selection = input("Enter the numbers of the items you want (comma-separated): ")
            return [int(x.strip()) for x in selection.split(",") if 1 <= int(x.strip()) <= len(grocery_items)]
        except ValueError:
            print("Invalid input. Please enter numbers separated by commas.")

def calculate_bags_needed(total_items):
    return max(1, (total_items + ITEMS_PER_BAG - 1) // ITEMS_PER_BAG)

global_cart = []

def main():
    print_store_menu()
    selected_items = get_user_selection()

    total_items = 0
    for item_num in selected_items:
        # Retrieve item details from grocery_items
        item_name, item_price, item_description = grocery_items[item_num - 1]
        quantity = int(input(f"How many {item_name} do you want? "))
        # Add item with description to global_cart
        global_cart.append(ItemToPurchase(item_name, item_price, quantity, item_description))
        total_items += quantity

    print("\n" + "="*40)
    print("Your Receipt")
    print("="*40)
    subtotal = 0
    for item in global_cart:
        item.print_item_cost()
        subtotal += item.item_price * item.item_quantity

    bags_needed = calculate_bags_needed(total_items)
    bag_charge = bags_needed * BAG_COST
    tax = subtotal * TAX_RATE
    total_cost = subtotal + bag_charge + tax

    print("-"*40)
    print(f"Subtotal:     ${subtotal:>6.2f}")
    print(f"Bag Charge:   ${bag_charge:>6.2f} ({bags_needed} bag{'s' if bags_needed > 1 else ''} @ ${BAG_COST:.2f} each)")
    print(f"Tax (9%):     ${tax:>6.2f}")
    print(f"Total:        ${total_cost:>6.2f}")
    print("="*40)
    print("Thank you for shopping with us!")

if __name__ == "__main__":
    main()
#week 6
grocery_items = [
    ("Apples", 0.50, "Fresh red apples"),
    ("Bananas", 0.30, "Ripe yellow bananas"),
    ("Bread", 2.00, "Whole wheat bread loaf"),
    ("Milk", 2.50, "1 gallon of whole milk"),
    ("Eggs", 3.00, "A dozen large eggs"),
    ("Cheese", 4.00, "Sharp cheddar cheese block"),
    ("Cereal", 3.50, "Whole grain cereal box"),
    ("Pasta", 1.50, "Dry spaghetti pasta"),
    ("Tomatoes", 1.00, "Fresh vine tomatoes"),
    ("Onions", 0.75, "Yellow onions"),
    ("Potatoes", 1.25, "Russet potatoes"),
    ("Chicken", 5.00, "Boneless chicken breast"),
    ("Beef", 6.00, "Ground beef"),
    ("Fish", 7.00, "Fresh salmon fillet"),
    ("Rice", 2.00, "Long-grain white rice"),
    ("Beans", 1.00, "Canned black beans"),
    ("Carrots", 0.75, "Fresh carrots"),
    ("Lettuce", 1.50, "Crisp romaine lettuce"),
    ("Yogurt", 2.00, "Greek yogurt"),
    ("Ice Cream", 4.50, "Vanilla ice cream"),
    ("Coffee", 5.00, "Ground coffee"),
    ("Tea", 3.00, "Herbal tea"),
    ("Juice", 2.50, "Orange juice"),
    ("Soda", 1.50, "Carbonated soft drink"),
    ("Chips", 2.00, "Potato chips"),
    ("Cookies", 2.50, "Chocolate chip cookies"),
    ("Candy", 1.00, "Mixed candy pack"),
    ("Chocolate", 2.00, "Dark chocolate bar"),
    ("Soap", 1.50, "Bar of soap"),
    ("Shampoo", 3.50, "Bottle of shampoo")
]

TAX_RATE = 0.09
BAG_COST = 0.08
ITEMS_PER_BAG = 5

# ItemToPurchase class definition
class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        total = self.item_price * self.item_quantity
        print(f"{self.item_name}: {self.item_quantity} @ ${self.item_price:.2f} = ${total:.2f}")

def print_store_menu():
    print("\n" + "="*40)
    print("Welcome to the Simple Grocery Store!")
    print("="*40)
    for i, (item, price, description) in enumerate(grocery_items, 1):
        print(f"{i:2}. {item:<15} ${price:.2f}")
        if i % 6 == 0:
            print()

def get_user_selection():
    while True:
        try:
            selection = input("Enter the numbers of the items you want (comma-separated): ")
            return [int(x.strip()) for x in selection.split(",") if 1 <= int(x.strip()) <= len(grocery_items)]
        except ValueError:
            print("Invalid input. Please enter numbers separated by commas.")

def calculate_bags_needed(total_items):
    return max(1, (total_items + ITEMS_PER_BAG - 1) // ITEMS_PER_BAG)

global_cart = []

def main():
    print_store_menu()
    selected_items = get_user_selection()

    total_items = 0
    for item_num in selected_items:
        # Retrieve item details from grocery_items
        item_name, item_price, item_description = grocery_items[item_num - 1]
        quantity = int(input(f"How many {item_name} do you want? "))
        # Add item with description to global_cart
        global_cart.append(ItemToPurchase(item_name, item_price, quantity, item_description))
        total_items += quantity

    print("\n" + "="*40)
    print("Your Receipt")
    print("="*40)
    subtotal = 0
    for item in global_cart:
        item.print_item_cost()
        subtotal += item.item_price * item.item_quantity

    bags_needed = calculate_bags_needed(total_items)
    bag_charge = bags_needed * BAG_COST
    tax = subtotal * TAX_RATE
    total_cost = subtotal + bag_charge + tax

    print("-"*40)
    print(f"Subtotal:     ${subtotal:>6.2f}")
    print(f"Bag Charge:   ${bag_charge:>6.2f} ({bags_needed} bag{'s' if bags_needed > 1 else ''} @ ${BAG_COST:.2f} each)")
    print(f"Tax (9%):     ${tax:>6.2f}")
    print(f"Total:        ${total_cost:>6.2f}")
    print("="*40)
    print("Thank you for shopping with us!")

if __name__ == "__main__":
    main()
