class Battery:
    def charge(self):
        print("Battery is charging")  # Battery starts charging

class Lights():
    def switch_on(self):
        print("Lights on")  # Lights are turned on

class Radio():
    def play_music(self):
        print("Playing music")  # Radio starts playing music

class ElectricCar:
    def __init__(self):
        self.battery = Battery()
        self.lights = Lights()
        self.radio = Radio()
        
    def drive(self):
        self.battery.charge()  # Call to charge battery
        self.lights.switch_on()  # Turn on the lights
        self.radio.play_music()  # Start playing music

my_tesla = ElectricCar()
my_tesla.drive()  # Activate car functions
