import random

class User:
    def __init__(self, username):
        self.username = username
        self.current_city = None
        self.destination_city = None

class Cab:
    def __init__(self, cab_id):
        self.cab_id = cab_id
        self.current_city = "DefaultCity"  # Default starting city
        self.is_available = True

class CabTravelApp:
    def __init__(self):
        self.users = []
        self.cabs = []

    def register_user(self, username):
        user = User(username)
        self.users.append(user)
        return user

    def display_menu(self):
        print("\nMenu:")
        print("1. Set current city")
        print("2. Request a ride")
        print("3. End the ride")
        print("4. Exit")

    def handle_user_input(self, user_input, user):
        if user_input == '1':
            current_city = input("Enter your current city: ")
            user.current_city = current_city
            print(f"Current city set to {user.current_city}")

        elif user_input == '2':
            if not user.current_city:
                print("Please set your current city first.")
                return
            destination_city = input("Enter destination city: ")
            self.request_ride(user, destination_city)

        elif user_input == '3':
            self.end_ride(user)

        elif user_input == '4':
            print("Exiting the application. Thank you!")
            exit()

        else:
            print("Invalid input. Please try again.")

    def request_ride(self, user, destination_city):
        available_cabs = [cab for cab in self.cabs if cab.is_available]
        if not available_cabs:
            print("Sorry, no cabs available at the moment. Please try again later.")
            return

        chosen_cab = random.choice(available_cabs)
        chosen_cab.is_available = False

        user.destination_city = destination_city

        print(f"Ride requested from {user.current_city} to {user.destination_city}.")
        print(f"Assigned cab {chosen_cab.cab_id}. Cab is on the way.")

    def end_ride(self, user):
        if not user.destination_city:
            print("You haven't requested a ride yet.")
            return

        print(f"Ride completed from {user.current_city} to {user.destination_city}.")
        user.current_city = user.destination_city
        user.destination_city = None

        # Make the cab available again
        assigned_cab = next((cab for cab in self.cabs if not cab.is_available), None)
        if assigned_cab:
            assigned_cab.is_available = True

# Sample usage
app = CabTravelApp()

# Register users
user1 = app.register_user("Alice")
user2 = app.register_user("Bob")

# Register cabs
cab1 = Cab(cab_id="C001")
cab2 = Cab(cab_id="C002")
app.cabs.extend([cab1, cab2])

while True:
    app.display_menu()
    user_input = input("Enter your choice (1-4): ")
    app.handle_user_input(user_input, user1)
