# Demonstrate encapsulation by creating a class with private attributes and
# use getter and setter methods to access/modify them.
class Person:
    def __init__(self, name, age):
        self.__name = name  # private attribute
        self.__age = age    # private attribute

    # Getter method for name
    def get_name(self):
        return self.__name

    # Setter method for name
    def set_name(self, name):
        self.__name = name

    # Getter method for age
    def get_age(self):
        return self.__age

    # Setter method for age
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Please enter a valid age")

# Example usage
person = Person("John", 30)
print(person.get_name())  # Output: John
print(person.get_age())   # Output: 30

person.set_name("Jane")
person.set_age(25)
print(person.get_name())  # Output: Jane
print(person.get_age())   # Output: 25

person.set_age(-5)  # Output: Please enter a valid age