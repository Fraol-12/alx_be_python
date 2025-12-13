import math

# Base Class
class Shape:
    def area(self):
        # This method is meant to be overridden by child classes
        raise NotImplementedError("Subclasses must override the area() method")


# Derived Class - Rectangle
class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Derived Class - Circle
class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


# Polymorphism Demo (optional but helpful)
if __name__ == "__main__":
    shapes = [
        Rectangle(10, 5),
        Circle(7),
        Rectangle(3, 8),
        Circle(2.5)
    ]

    for shape in shapes:
        print(f"{shape.__class__.__name__} area:", shape.area())