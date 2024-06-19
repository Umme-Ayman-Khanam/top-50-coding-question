class Movie:
    def __init__(self, title):
        self.title = title

class Theater:
    def __init__(self):
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def display_movies(self):
        print("Available Movies:")
        for i, movie in enumerate(self.movies, start=1):
            print(f"{i}. {movie.title}")

class TicketBookingSystem:
    def __init__(self):
        self.theater = Theater()
        self.booked_seats = set()
        self.ticket_price = 250  

    def book_ticket(self, movie_index, num_tickets):
        if 1 <= movie_index <= len(self.theater.movies):
            selected_movie = self.theater.movies[movie_index - 1]
            print(f"\nBooking tickets for {selected_movie.title}...")

            available_seats = 50  
            if available_seats >= num_tickets:
                total_price = self.calculate_total_price(num_tickets)
                print(f"Total Price: Rs {total_price}")

                for i in range(num_tickets):
                    seat_number = self.get_available_seat()
                    self.booked_seats.add(seat_number)
                    print(f"Ticket booked! Seat Number: {seat_number}")
            else:
                print("Sorry, not enough seats available.")
        else:
            print("Invalid movie selection.")

    def calculate_total_price(self, num_tickets):
        return num_tickets * self.ticket_price

    def get_available_seat(self):
        seat_number = 1
        while seat_number in self.booked_seats:
            seat_number += 1
        return seat_number

def main():

    movie1 = Movie("Inception")
    movie2 = Movie("The Dark Knight")

    theater = Theater()
    theater.add_movie(movie1)
    theater.add_movie(movie2)
    ticket_system = TicketBookingSystem()
    ticket_system.theater = theater

    while True:
        
        theater.display_movies()

    
        try:
            movie_index = int(input("\nEnter the number of the movie you want to watch: "))
            num_tickets = int(input("Enter the number of tickets you want to book: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        ticket_system.book_ticket(movie_index, num_tickets)

        cont = input("\nDo you want to book more tickets? (yes/no): ").lower()
        if cont != 'yes':
            print("Thank you for using the ticket booking system. Enjoy the movie!")
            break

if __name__ == "__main__":
    main()
