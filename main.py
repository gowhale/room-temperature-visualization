from time import sleep
from random import randrange
import datetime

# Custom Classes
from weather_api import Weather
from sensor import Sensor
from readings_log import ReadingsLog

#CONSTANTS
TIME_BETWEEN_READINGS = 60   # Seconds between readings

INCLUDE_WEATHER = True      # Call the API to include weather data in report?
CURRENT_CITY = "CARDIFF"    # City for weather


def pretty_time(raw_datetime):
    return (raw_datetime.strftime("%H:%M:%S"))


def pretty_date(raw_datetime):
    return (raw_datetime.strftime("%Y:%m:%d"))


def get_current_time_object():
    current_date_time = datetime.datetime.now()

    return current_date_time


def main():

    current_file = ReadingsLog(INCLUDE_WEATHER)

    for _ in range(100):

        enviroment_reader = Sensor()
        temperature = enviroment_reader.get_temperature()
        humidity = enviroment_reader.get_humidity()
        pressure = enviroment_reader.get_pressure()
        current_time = get_current_time_object()
        row = [pretty_time(current_time), str(temperature),
               str(humidity), str(pressure)]

        if (INCLUDE_WEATHER):
            current_weather = Weather(CURRENT_CITY)
            row.append(str(current_weather.get_ceclius_temp()))
            row.append(str(current_weather.get_weather_description()))

        current_file.append_row(row)

        sleep(TIME_BETWEEN_READINGS)


if __name__ == "__main__":
    # execute only if run as a script
    main()
