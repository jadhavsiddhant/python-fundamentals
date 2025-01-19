# Modify the Car class to have default values for make and model if not
# provided.
class Car:
    def __init__(self, make="Toyota", model="Corolla"):
        self.make = make
        self.model = model