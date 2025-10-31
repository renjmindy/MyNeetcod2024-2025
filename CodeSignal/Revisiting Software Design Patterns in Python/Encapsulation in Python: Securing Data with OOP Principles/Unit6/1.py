# TODO: Define a class named DrawingApplication. It should have methods to add shapes and draw all added shapes.
class DrawingApplication:
    def __init__(self):
        self.shapes = list()
    def add_shapes(self, shape):
        self.shapes.append(shape)
    def draw(self):
        for shape in self.shapes:
            shape.draw()
# TODO: Define a class for Circle with a draw method that prints "Circle drawn with polymorphism!"
class Circle:
    def draw(self):
        print("Circle drawn with polymorphism!")
# TODO: Define a class for Square with a draw method that prints "Square drawn with polymorphism!"
class Square:
    def draw(self):
        print("Square drawn with polymorphism!")

# Instantiate DrawingApplication
drawapp = DrawingApplication()
# TODO: Create instances of Circle and Square
circle = Circle()
square = Square()
# TODO: Add these shape instances to the DrawingApplication instance
drawapp.add_shapes(circle)
drawapp.add_shapes(square)
# TODO: Call the method of DrawingApplication to draw all shapes
drawapp.draw()
# Remember to comment on your design choices related to Encapsulation, Polymorphism, and Composition
