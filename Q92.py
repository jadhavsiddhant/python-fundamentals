# In the Dog class, override a method speak defined in Animal (e.g., Animal
# says “Some sound”, but Dog says “Woof!”).
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

# Example usage
dog = Dog()
print(dog.speak())  # Output: Woof!