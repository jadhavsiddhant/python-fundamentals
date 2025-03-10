#  Create classes Rectangle and Square. Square should inherit from
# Rectangle (or implement composition) in a way that automatically sets the
# length and width to the same value.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)