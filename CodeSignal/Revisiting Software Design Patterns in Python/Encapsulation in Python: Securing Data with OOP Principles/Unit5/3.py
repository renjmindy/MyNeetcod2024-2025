# TODO: Define a base class named Shape. It should be designed to be sub-classed but not instantiated directly.
class Shape:
    def draw(self):
        pass
        
class Rectangle(Shape):
    def draw(self):
        print("this is rectangle")

class Circle(Shape):
    def draw(self):
        print("this is circle")
        
class Composite:
    def __init__(self):
        self.shapes = list()
    def add_shape(self, shape):
        self.shapes.append(shape)
    def draw(self):
        for shape in self.shapes: shape.draw()
        
rect = Rectangle()
circ = Circle()
comp = Composite()
comp.add_shape(rect)
comp.add_shape(circ)
comp.draw()
# TODO: Implement at least two derived classes (e.g., Rectangle, Circle), each with a draw() method that prints a message indicating what it is drawing.

# TODO: Define a class that acts as a composite for the shape objects. It should be capable of storing multiple shape instances and calling their draw() method.

# TODO: Create instances of your derived shapes, add them to the composite object, and then render them through a method call to the composite.

# In the comments below, explain why you chose the design pattern you implemented:
# TODO: add your comments here
