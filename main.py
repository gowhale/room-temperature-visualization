from time import sleep
from random import randrange
import datetime

# Custom Classes
from weather_api import Weather

try:
    from sensor import Sensor
except FileNotFoundError:
    print("SENSOR ERROR, ENSURE INSTALLATION COMPLETE")

from readings_log import ReadingsLog

# CONSTANTS
TIME_BETWEEN_READINGS = 60*5   # Seconds between readings

INCLUDE_WEATHER = True      # Call the API to include weather data in report?
CURRENT_CITY = "CARDIFF"    # City for weather


def pretty_time(raw_datetime):
    """converts datetime object into time in string format"""
    return (raw_datetime.strftime("%H:%M:%S"))


def pretty_date(raw_datetime):
    """converts datetime object into date in string format"""
    return (raw_datetime.strftime("%Y:%m:%d"))


def get_current_time_object():
    """Fetches current datetime in datetime object"""
    current_date_time = datetime.datetime.now()
    return current_date_time


def main():
    """Takes sensor and weather readings at constant rate, saves to CSV."""

    current_file = ReadingsLog(INCLUDE_WEATHER)

    for _ in range(100):

        current_time = get_current_time_object()
        try:
            enviroment_reader = Sensor()
            temperature = enviroment_reader.get_temperature()
            humidity = enviroment_reader.get_humidity()
            pressure = enviroment_reader.get_pressure()
            row = [pretty_time(current_time), str(temperature),
                   str(humidity), str(pressure)]
        except FileNotFoundError:
            print("SENSOR ERROR, ENSURE INSTALLATION COMPLETE")
            row = [pretty_time(current_time), "SENSOR ERROR",
                   "SENSOR ERROR", "SENSOR ERROR"]
        except NameError:
            print("SENSOR ERROR, CANNOT CREATE CLASS AS IMPORT FAILED")
            row = [pretty_time(current_time), "SENSOR ERROR",
                   "SENSOR ERROR", "SENSOR ERROR"]

        if (INCLUDE_WEATHER):
            try:
                current_weather = Weather(CURRENT_CITY)
                row.append(str(current_weather.get_ceclius_temp()))
                row.append(str(current_weather.get_weather_description()))
            except NameError:
                print(
                    "WEATHER API ERROR. weather_api_key is not defined, CREATE secrets.py THEN ADD weather_api_key STRING")
                row.append("WEATHER API ERROR")
                row.append("WEATHER API ERROR")

        current_file.append_row(row)

        sleep(TIME_BETWEEN_READINGS)


if __name__ == "__main__":
    # execute only if run as a script
    main()
