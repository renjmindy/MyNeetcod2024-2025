class WeatherService:
    def get_current_weather(self):
        # Assuming this method originally returns 20
        return 20  # Temperature in Celsius as an integer

class WeatherServiceAdapter():
    def __init__(self):
        self.weather = WeatherService()
# TODO: Implement the integration with a new weather data provider.
# TODO: Ensure that get_current_weather() remains usable for clients relying on the current temperature.
# TODO: Introduce a get_detailed_weather() method that returns detailed weather information.
    def get_current_weather(self):
        return self.weather.get_current_weather()
        
    def get_detailed_weather(self):
        return {
            "temperature": self.weather.get_current_weather(),
            "pressure": 1013,
            "humidity": 75
        }
