# Demonstrate multiple inheritance with two parent classes providing
# different functionalities to a child class.
class Parent1:
    def function1(self):
        return "Functionality from Parent1"

class Parent2:
    def function2(self):
        return "Functionality from Parent2"

class Child(Parent1, Parent2):
    pass

child_instance = Child()
print(child_instance.function1())
print(child_instance.function2())