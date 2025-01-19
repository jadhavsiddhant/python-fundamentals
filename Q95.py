# Demonstrate polymorphism by defining a method draw() in multiple
# classes (Circle, Triangle, etc.) and calling draw() on a list of shapes.
class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Drawing a Circle")

class Triangle(Shape):
    def draw(self):
        print("Drawing a Triangle")

shapes = [Circle(), Triangle()]

for shape in shapes:
    shape.draw()