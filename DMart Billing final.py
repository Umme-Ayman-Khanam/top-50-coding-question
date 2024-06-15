class Supermarket:
    def __init__(self):
        self.products = {
            'grocery': {'rice': 50, 'flour': 60, 'sugar': 50.0},
            'kitchen': {'knife': 100.0, 'pan': 800.0, 'spoon': 150.0},
            'clothes': {'shirt': 250.0, 'pants': 500.0, 'socks': 200.0}
        }
        self.cart = {}

    def display_menu(self):
        print("Shopping Categories:")
        print("a. Grocery")
        print("b. Kitchen")
        print("c. Clothes")

    def display_products(self, category):
        print(f"Available products in {category.capitalize()} category:")
        for product, price in self.products[category].items():
            print(f"{product}: Rs {price:.2f}")

    def verify_product(self, category, product):
        if product in self.products[category]:
            return True
        else:
            return False

    def add_to_cart(self, category, product, quantity):
        if category not in self.cart:
            self.cart[category] = {}

        if product not in self.cart[category]:
            self.cart[category][product] = 0

        self.cart[category][product] += quantity

    def calculate_total(self):
        total = 0
        print("\nYour Cart:")
        for category, products in self.cart.items():
            print(f"\nCategory: {category.capitalize()}")
            for product, quantity in products.items():
                price = self.products[category][product]
                total += price * quantity
                print(f"{product} x{quantity} - Rs {price * quantity:.2f}")

        print("\nTotal Bill: Rs {:.2f}".format(total))

    def run(self):
        print("Welcome to the Supermarket Billing System!")

        while True:
            self.display_menu()
            category = input("Select a category (a, b, c) or press 'q' to quit: ")

            if category.lower() == 'q':
                break

            if category in ['a', 'b', 'c']:
                category_key = {'a': 'grocery', 'b': 'kitchen', 'c': 'clothes'}[category]
                self.display_products(category_key)

                product = input("Enter the product you want to buy: ")
                if self.verify_product(category_key, product):
                    quantity = int(input("Enter the quantity: "))
                    self.add_to_cart(category_key, product, quantity)
                    print(f"{quantity} {product}(s) added to your cart.")
                else:
                    print("Product not available in the selected category. Please try again.")
            else:
                print("Invalid category. Please try again.")

        if self.cart:
            self.calculate_total()
            print("Thank you for shopping with us! Have a great day.")
        else:
            print("No items were added to the cart. Goodbye!")


if __name__ == "__main__":
    supermarket = Supermarket()
    supermarket.run()


