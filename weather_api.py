from secrets import weather_api_key
import requests
import json


class Weather:

    def __init__(self, city_name):
        self.city_name = city_name
        self.read_weather()

    def create_celcius_temp(self):
        raw_celcius = (self.kelvin_temp - 273.15)
        formatted_celcius = round(raw_celcius, 2)
        self.celcius_temp = formatted_celcius

    def read_weather(self):
        base_url = "http://api.openweathermap.org/data/2.5/weather?"

        complete_url = base_url + "appid=" + weather_api_key + "&q=" + self.city_name

        response = requests.get(complete_url)

        pretty_json = response.json()

        try:

            main_data = pretty_json["main"]

            current_temperature_kelvin = main_data["temp"]
            self.kelvin_temp = current_temperature_kelvin
            self.create_celcius_temp()

        except KeyError:

            error_code = str(pretty_json["cod"])

            if error_code == '404':

                print(" --- City Not Found  --- ")

            if error_code == '401':

                print(" --- API KEY ERROR --- ")

            else:
                print("UNKNOWN ERROR CODE")

    def get_ceclius_temp(self):
        return self.celcius_temp

    def get_kelvin_temp(self):
        return self.kelvin_temp
