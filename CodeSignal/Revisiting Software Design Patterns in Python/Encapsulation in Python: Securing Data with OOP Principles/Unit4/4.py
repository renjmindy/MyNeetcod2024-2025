# Define a class for the Auxiliary Power Unit. It should have a method to generate power.
class Auxiliary:
    def generate_power(self):
        print("Start the engine!!!")
        
class Lighting:
    def illuminate(self):
        print("Lightening up!!!")
        
class Avionics:
    def navigation(self):
        print("Navigation systems check!!!")
        
class Aircraft:
    def __init__(self):
        self.auxiliary = Auxiliary()
        self.light = Lighting()
        self.avionics = Avionics()
        
    def takeoff(self):
        self.auxiliary.generate_power()
        self.light.illuminate()
        self.avionics.navigation()
        
airplane = Aircraft()
airplane.takeoff()
# Define a class for the Lighting System. It should have a method to illuminate.

# Define a class for the Avionics. It should have a method to perform a navigation systems check.

# Define a class for the Aircraft that uses the above components. Ensure it prepares the aircraft for takeoff.

# Create an instance of the Aircraft and call its method to prepare for takeoff.
