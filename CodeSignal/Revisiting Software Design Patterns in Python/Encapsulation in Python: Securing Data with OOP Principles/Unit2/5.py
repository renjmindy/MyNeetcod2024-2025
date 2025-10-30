from abc import ABC, abstractmethod

# TODO: Define an abstract class named SmartDevice with power_on and power_off methods.
class SmartDevice(ABC):
    @abstractmethod
    def power_on(self):
        pass
    @abstractmethod
    def power_off(self):
        pass
        
# TODO: Create a Sensor class inheriting from SmartDevice, adding an abstract method read_data.
class Sensor(SmartDevice):
    @abstractmethod
    def read_data(self):
        pass
        
# TODO: Implement TemperatureSensor class.
class TemperatureSensor(Sensor):
    def __init__(self, calibration_factor):
        self.calibration_factor = calibration_factor
    def power_on(self):
        pass
    def power_off(self):
        pass
    def read_data(self):
        self.temp = 20 * self.calibration_factor
        return self.temp
# It should initialize with a calibration_factor, and define power_on, power_off, and read_data methods.
# Use a standard temperature of 20 degrees Celsius and adjust by calibration_factor in the read_data method.

# TODO: Implement MotionSensor class.
class MotionSensor(Sensor):
    def power_on(self):
        self.sensitivity_level = 20
    def power_off(self):
        self.sensitivity_level = 0
    def read_data(self):
        self.motion_detection = self.sensitivity_level
        return self.motion_detection
# It should override power_on to set a sensitivity level and define power_off, and read_data methods to simulate motion detection.
