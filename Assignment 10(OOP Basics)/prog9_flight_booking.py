"""
Program 9: Create a Flight class with seat booking functionality.
"""

class Flight:
    def __init__(self, flight_number, destination, total_seats):
        self.flight_number = flight_number
        self.destination = destination
        self.total_seats = total_seats
        self.booked_seats = 0

    def available_seats(self):
        return self.total_seats - self.booked_seats

    def book_seats(self, num_seats):
        if num_seats <= 0:
            print("Please enter a valid number of seats to book.")
        elif num_seats <= self.available_seats():
            self.booked_seats += num_seats
            print(f"Successfully booked {num_seats} seat(s) for flight {self.flight_number} to {self.destination}.")
            print(f"Remaining available seats: {self.available_seats()}/{self.total_seats}")
        else:
            print(f"Booking failed! Only {self.available_seats()} seat(s) available on flight {self.flight_number}.")

    def cancel_seats(self, num_seats):
        if 0 < num_seats <= self.booked_seats:
            self.booked_seats -= num_seats
            print(f"Cancelled {num_seats} seat(s). Available seats: {self.available_seats()}/{self.total_seats}")
        else:
            print("Invalid cancellation request.")

    def flight_info(self):
        print(f"Flight: {self.flight_number} -> {self.destination} | Total Seats: {self.total_seats} | Booked: {self.booked_seats} | Available: {self.available_seats()}")


def main():
    print("--- Program 9: Flight Class Seat Booking ---")
    flight = Flight(flight_number="AI-202", destination="New York", total_seats=5)
    flight.flight_info()

    print()
    flight.book_seats(3)
    flight.book_seats(3)  # Exceeds available seats
    flight.cancel_seats(1)
    flight.book_seats(3)  # Now available


if __name__ == "__main__":
    main()
