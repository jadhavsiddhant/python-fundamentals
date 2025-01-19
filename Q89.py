# Define a class Car with a constructor that sets make, model, and year.
# Create an instance and display its details.
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_details(self):
        print(f"Car Make: {self.make}")
        print(f"Car Model: {self.model}")
        print(f"Car Year: {self.year}")

# Create an instance of the Car class
my_car = Car("Toyota", "Corolla", 2020)

# Display the details of the car
my_car.display_details()