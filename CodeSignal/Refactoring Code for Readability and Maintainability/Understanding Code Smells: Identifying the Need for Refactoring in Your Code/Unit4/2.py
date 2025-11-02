class WeatherSystem:
    def get_weather_summary(self, date, version):
        # TODO: Implement the logic to call the correct version of the weather summary based on the passed version number.
        if version == 1: return self.weather_summary_v1(date)
        if version == 2: return self.weather_summary_v2(date)
        

    def weather_summary_v1(self, date):
        # Dummy data for demonstration
        high_temp, low_temp = 25, 18
        return f"High: {high_temp}C, Low: {low_temp}C"

    # TODO: Implement weather_summary_v2 here to include high and low temperatures, chance of precipitation, and wind speed.
    def weather_summary_v2(self, date):
        high_temp, low_temp, chance_of_precipitation, wind_speed = 25, 18, 50, 15
        return f"High: {high_temp}C, Low: {low_temp}C, Precipitation: {chance_of_precipitation}%, Wind Speed: {wind_speed}km/h"
    # Expected Output: "High: 25C, Low: 18C, Precipitation: 50%, Wind Speed: 15km/h"
