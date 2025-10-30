from abc import ABC, abstractmethod

# TODO: Define an abstract class named HomeAppliance with an abstract method power_on
class HomeAppliance(ABC):
    @abstractmethod
    def power_on(self):
        pass
    
# TODO: Design a Refrigerator class inheriting HomeAppliance, implementing the power_on method to indicate it's cooling.
class Refrigerator(HomeAppliance):
    
    def power_on(self):
        return "refrigerator is cooling"

# TODO: Create an Oven class inheriting HomeAppliance, with a power_on method indicating it's heating.
class Oven(HomeAppliance):
    
    def power_on(self):
        return "oven is heating"

# TODO: Instantiate both Refrigerator and Oven, invoking the power_on method for each to demonstrate functionality.
refrigerator = Refrigerator()
oven = Oven()
print(refrigerator.power_on())
print(oven.power_on())
