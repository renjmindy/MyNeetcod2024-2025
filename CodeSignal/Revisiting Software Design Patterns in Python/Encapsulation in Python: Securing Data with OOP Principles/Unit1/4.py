class TemperatureSensor:
    def __init__(self):
        self.__temperature = 0    # Private attribute for temperature

    def get_temperature(self):   # Getter method for temperature
        return self.__temperature

    def __update_temperature(self, new_temp):  # Private setter method
        # TODO: Write logic to update temperature only if it's in the range -50 to 150 degrees
        #pass
        if new_temp >= -50 and new_temp <= 150: self.__temperature = new_temp

    # TODO: Implement the method `measure_temp` to simulate temperature measurement and update temperature
    # You can use `random` module to simulate temperature measurement
    def measure_temp(self):
        from random import randint
        self.__update_temperature(randint(-1000, 1000))

sensor = TemperatureSensor()
sensor.measure_temp()
print(f"Measured Temperature: {sensor.get_temperature()}°C")
