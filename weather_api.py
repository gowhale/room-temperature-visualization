try:
    from secrets import weather_api_key
except ImportError:
    print("NO SECRETS FILE DETECTED. CREATE secrets.py THEN ADD weather_api_key STRING")
except FileNotFoundError:
    print("NO SECRETS FILE DETECTED. CREATE secrets.py THEN ADD weather_api_key STRING")


import requests
import json


class Weather:
    """This class represents the weather which is fetched from the openweathermap API"""

    def __init__(self, city_name):
        """Initialises the object and sets the object city_name.

        Keyword arguments:
        city_name -- the current city the device is in i.e. Cardiff, London etc
        """
        self.city_name = city_name
        self.read_weather()

    def create_celcius_temp(self):
        """Converts object's kelvin value to celcius"""
        raw_celcius = (self.kelvin_temp - 273.15)
        formatted_celcius = round(raw_celcius, 2)
        self.set_ceclius_temp(formatted_celcius)

    def read_weather(self):
        """Requests data from the open weather api. Requires secret to be defined in a secrets.py file"""

        base_url = "http://api.openweathermap.org/data/2.5/weather?"

        complete_url = base_url + "appid=" + weather_api_key + "&q=" + self.city_name

        response = requests.get(complete_url)

        pretty_json = response.json()
        self.pretty_json = pretty_json

        try:

            main_data = pretty_json["main"]

            current_temperature_kelvin = main_data["temp"]

            self.set_kelvin_temp(current_temperature_kelvin)
            self.create_celcius_temp()
            self.set_weather_description(
                pretty_json["weather"][0]['description'])

        except KeyError:

            error_code = str(pretty_json["cod"])

            if error_code == '404':

                print(" --- City Not Found  --- ")

            if error_code == '401':

                print(" --- API KEY ERROR --- ")

            else:
                print("UNKNOWN ERROR CODE")

    def get_ceclius_temp(self):
        """Gets the temp of weather in celcius"""
        return self.celcius_temp

    def get_kelvin_temp(self):
        """Gets the temp of weather in kelvin"""
        return self.kelvin_temp

    def get_weather_description(self):
        """Gets description of the weather"""
        return self.weather_description

    def set_ceclius_temp(self, c):
        """Sets the temp of weather in celcius"""
        self.celcius_temp = c

    def set_kelvin_temp(self, k):
        """Sets the temp of weather in kelvin"""
        self.kelvin_temp = k

    def set_weather_description(self, description):
        """Sets description of the weather"""
        self.weather_description = description
