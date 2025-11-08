class Light:
    def turnOn(self):
        print("Light turned on")

    def turnOff(self):
        print("Light turned off")

class Thermostat:
    def setTemperature(self, degrees):
        print(f"Temperature set to {degrees} degrees Celsius")

class SecurityCamera:
    def enable(self):
        print("Security camera enabled")

    def disable(self):
        print("Security camera disabled")

class SmartHomeFacade:
    def __init__(self, lights, thermostat, cameras):
        self.lights = lights
        self.thermostat = thermostat
        self.cameras = cameras

    # TODO: Implement a method `leavingHome()` that turns off all lights sets the thermostat to 18 degrees, 
    # enables all security cameras, and prints "Leaving home procedure executed"
    def leavingHome(self):
        for light in self.lights:
            light.turnOff()
        self.thermostat.setTemperature(18)
        for camera in self.cameras:
            camera.enable()
        print("Leaving home procedure executed")

    # TODO: Implement a method `arriveHome()` that turns on all lights,
    # sets the thermostat to 22 degrees, disables all security cameras, and prints "Arrive home procedure executed"
    def arriveHome(self):
        for light in self.lights:
            light.turnOn()
        self.thermostat.setTemperature(22)
        for camera in self.cameras:
            camera.disable()
        print("Arrive home procedure executed")
