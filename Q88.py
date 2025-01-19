# Add a method greet to the Person class that prints "Hello, my name is
# <name>".
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}")