class FoodOrderingApp:
    def __init__(self):
        self.menu = {
            '1': {'name': 'Burger', 'price': 60.0},
            '2': {'name': 'Pizza', 'price': 120.0},
            '3': {'name': 'Pasta', 'price': 100.0},
            '4': {'name': 'Fries', 'price': 80.0},
        }
        self.order = []

    def display_menu(self):
        print("Menu:")
        for item_id, item_info in self.menu.items():
            print(f"{item_id}. {item_info['name']} - Rs {item_info['price']}")

    def place_order(self):
        self.display_menu()
        while True:
            choice = input("Enter the item number you want to order (press 'q' to quit): ")
            if choice.lower() == 'q':
                break
            elif choice in self.menu:
                quantity = int(input(f"How many {self.menu[choice]['name']}s do you want? "))
                self.order.append({'item': self.menu[choice]['name'], 'quantity': quantity, 'price': self.menu[choice]['price'] * quantity})
            else:
                print("Invalid choice. Please try again.")

    def display_order(self):
        if not self.order:
            print("Your order is empty.")
        else:
            print("Your order is confirmed!")
            total_price = 0
            for item in self.order:
                print(f"{item['item']} x{item['quantity']} - Rs {item['price']:.2f}")
                total_price += item['price']
            print(f"Total: Rs {total_price:.2f}")

    def run(self):
        print("Welcome to the Food Ordering App!")
        while True:
            print("\n1. Place an order\n2. View your order\n3. Quit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.place_order()
            elif choice == '2':
                self.display_order()
            elif choice == '3':
                print("Thank you for using the Food Ordering App. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    app = FoodOrderingApp()
    app.run()
