# TODO: Define a class for the GPU. It should have a method to render graphics.
class GPU:
    def render_graphics(self):
        print("rendering graphs!!!")
class RAM:
    def load_data(self):
        print("loading data!!!")
class Motherboard:
    def __init__(self):
        self.gpu = GPU()
        self.ram = RAM()
    def process_tasks(self):
        self.gpu.render_graphics()
        self.ram.load_data()
class ComputerSystem:
    def __init__(self):
        self.motherboard = Motherboard()
    def call_tasks(self):
        self.motherboard.process_tasks()
        
system = ComputerSystem()
system.call_tasks()
# TODO: Define a class for the RAM. It should have a method to load data.

# TODO: Define a class for the Motherboard. Remember, it includes both GPU and RAM.
# MotherBoard must have a `process_tasks` method that calls the methods from the GPU and RAM classes

# TODO: Define a method for the Motherboard to process tasks. It should render graphics and load data.

# TODO: Define a class for the ComputerSystem that includes the Motherboard.

# TODO: Define a method for the ComputerSystem to run and utilize the Motherboard to process tasks.

# TODO: Create an instance of the ComputerSystem and call its run method.
