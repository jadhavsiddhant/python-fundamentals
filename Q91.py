# Create a base class Animal and a derived class Dog. The Dog class should
# inherit attributes and methods from Animal.
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Example usage
dog = Dog("Buddy")
print(dog.speak())