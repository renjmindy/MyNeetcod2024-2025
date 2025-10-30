class GraphicShape:
    def paint(self):
        pass

class Triangle(GraphicShape):
    def __init__(self, base, height):
        # TODO: implement constructor
        self.base = base
        self.height = height

    def paint(self):  # Polymorphic method for Triangle
        # TODO: Return a string describing how a triangle is painted, including its base and height
        return f"describing how a triangle is painted, including its {self.base} and {self.height}"

class Ellipse(GraphicShape):
    def __init__(self, major_axis, minor_axis):
        # TODO: implement constructor
        self.major_axis = major_axis
        self.minor_axis = minor_axis

    def paint(self):  # Polymorphic method for Ellipse
        # TODO: Return a string describing how an ellipse is painted including its major and minor axes
        return f"describing how an ellipse is painted including its {self.major_axis} and {self.minor_axis} axes"

# Instantiate shapes
shapes = [Triangle(10, 5), Ellipse(7, 3)]

# Polymorphic behavior demonstration
for shape in shapes:
    print(shape.paint())  # Expect unique painting messages for each shape
