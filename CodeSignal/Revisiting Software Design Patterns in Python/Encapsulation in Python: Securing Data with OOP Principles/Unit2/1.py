from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def get_fuel_type(self):
        pass

class ElectricCar(Vehicle):
    def __init__(self):
        self.fuel_type = "electricity"

    def fuel_type(self):
        return self.fuel_type
        
    def get_fuel_type(self):
        return self.fuel_type

tesla = ElectricCar()  
print(tesla.get_fuel_type())
