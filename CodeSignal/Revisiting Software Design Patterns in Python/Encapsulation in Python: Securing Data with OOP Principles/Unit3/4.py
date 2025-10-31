# TODO: Define a base class named GraphicShape with a method identify that does nothing
class GraphicsShape:
    def identify(self):
        pass
# TODO: Define a subclass of GraphicShape named Pentagon with its identify method returning "I am a Pentagon with 5 sides."
class Pentagon(GraphicsShape):
    def identify(self):
        return "I am a Pentagon with 5 sides."

# TODO: Define another subclass of GraphicShape named Hexagon with its identify method returning "I am a Hexagon with 6 sides."
class Hexagon(GraphicsShape):
    def identify(self):
        return "I am a Hexagon with 6 sides."
# TODO: Create a list named shapes containing instances of Pentagon and Hexagon
shapes = [Pentagon(), Hexagon()]
# TODO: Use a loop to iterate over each shape in the shapes list and print its identify method's return value
for shape in shapes:
    print(shape.identify())
