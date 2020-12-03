from secrets import weather_api_key

import requests
import json

def kelvin_to_celcius (k):
    raw_value = (k - 273.15)
    formatted_value = round(raw_value,2)
    return formatted_value


def get_weather(city_name):
    print("Weather Getter")

    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    complete_url = base_url + "appid=" + weather_api_key + "&q=" + city_name

    response = requests.get(complete_url)

    pretty_json = response.json()

    try:

        main_data = pretty_json["main"]

        current_temperature_kelvin = main_data["temp"]
        current_temperature_celcius = kelvin_to_celcius(current_temperature_kelvin)

        # print(" Temperature (in kelvin unit) = " +

        #       str(current_temperature_kelvin) +

        #       "\n Temperature (in celcius unit) = " +
              
        #       str(current_temperature_celcius))

    except KeyError:

        error_code = str(pretty_json["cod"])

        if error_code == '404':

            print(" --- City Not Found  --- ")

        if error_code == '401':

            print(" --- API KEY ERROR --- ")

        else:
            print("ERROR")
            print(pretty_json)

    return current_temperature_celcius


# get_weather("CARDIFF")
