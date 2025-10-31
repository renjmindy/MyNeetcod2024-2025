class Processor:
    def compute(self):
        print("Processor is computing tasks")

class Memory:
    def store_data(self):
        print("Memory is storing data")

class Motherboard:
    def __init__(self):
        # TODO: Initialize the Processor and Memory as components of the Motherboard
        #pass
        self.processor = Processor()
        self.memory = Memory()

    def execute(self):
        self.processor.compute()
        self.memory.store_data()

class Computer:
    def __init__(self):
        self.motherboard = Motherboard()

    # TODO: Define the start method for the Computer to print a starting message and execute motherboard tasks
    def start(self):
        print("Computer is starting\n")
        self.motherboard.execute()

my_computer = Computer()
my_computer.start()  # Start the computer and its components
