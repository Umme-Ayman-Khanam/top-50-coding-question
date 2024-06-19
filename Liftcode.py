class Lift:
    current_floor = 1


    def move_to_floor(self, call_floor):
        if call_floor > 1 and call_floor < 6:
            print(f"Moving the lift from floor {self.current_floor} to floor {call_floor}.")
            self.current_floor = call_floor
        elif call_floor == self.current_floor:
            print(f"Lift is already on floor {call_floor}.")
        else:
            print("Invalid floor number. Please select a floor above the ground floor.")
def main():
    lift = Lift()

    while True:
        print("\nLift Control Panel[Floor 1-5]:")
        print(f"Current Floor: {lift.current_floor}")
        print("1. Call Lift")
        print("2. Move to Floor")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            call_floor = int(input("Enter your current floor to call the lift: "))
            lift.move_to_floor(call_floor)

        elif choice == "2":
            destination_floor = int(input("Enter the floor you want to go to: "))
            lift.move_to_floor(destination_floor)

        elif choice == "3":
            print("Exiting the lift control panel. Have a nice day!")
            break

        else:
            print("Invalid choice. Please select a valid option.")




if __name__ == "__main__":
    main()


