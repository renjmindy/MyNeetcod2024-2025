class GraphicObject:
    def draw(self):
        pass

class Circle(GraphicObject):
    # TODO: Implement required method(s) so they return a string indicating a circle is being drawn
    def draw(self):
        return "a circle is being drawn"

class Square(GraphicObject):
    # TODO: Implement required method(s) so they return a string indicating a square is being drawn
    def draw(self):
        return "a square is being drawn"

# TODO: Build a list `shapes` of graphic objects - circles and squares
shapes = [Circle(), Square()]
for shape in shapes:
    print(shape.draw())  # Polymorphism enables different draw behaviors
