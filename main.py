import csv
from time import sleep
from random import randrange
import datetime
from weather_api import get_weather
from sensor import Sensor

TIME_BETWEEN_READINGS = 1   # Seconds between readings

INCLUDE_WEATHER = False      # Call the API to include weather data in report?
CURRENT_CITY = "CARDIFF"    # City for weather


# def get_temperature():
#     # TODO: get temperature from rasbperry pi sensor rather than just random number

#     return temperature


# def get_humidity():
#     # TODO: get humidity from rasbperry pi sensor rather than just random number
#     (chip_id, chip_version) = readBME280ID()
#     print("Chip ID     :", chip_id)
#     print("Version     :", chip_version)

#     temperature, pressure, humidity = readBME280All()

#     print("Temperature : ", temperature, "C")
#     print("Pressure : ", pressure, "hPa")
#     print("Humidity : ", humidity, "%")
#     return humidity


def pretty_time(raw_datetime):
    return (raw_datetime.strftime("%H:%M:%S"))


def pretty_date(raw_datetime):
    return (raw_datetime.strftime("%Y:%m:%d"))


def get_current_time_object():
    current_date_time = datetime.datetime.now()

    return current_date_time


def create_csv():
    headers = [["time", "temperature", "humidity", "pressure"]]
    if (INCLUDE_WEATHER):
        headers[0].append(get_weather(CURRENT_CITY))
    current_datetime = get_current_time_object()
    file_name = ("reports/temperature-report-{}-{}.csv").format(pretty_date(current_datetime),
                                                                pretty_time(current_datetime))
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(headers)

    return file_name


def main():
    # TODO : capture enviroment temp and visualise data

    current_file = create_csv()

    for _ in range(100):
        enviroment_reader = Sensor()
        temperature = enviroment_reader.get_temperature()
        humidity = enviroment_reader.get_humidity()
        pressure = enviroment_reader.get_pressure()
        current_time = get_current_time_object()
        row = [pretty_time(current_time), str(temperature),
               str(humidity), str(pressure)]

        if (INCLUDE_WEATHER):
            row.append(get_weather(CURRENT_CITY))

        print(row)
        file = open(current_file, 'a')
        row_str = ",".join(row)+"\n"
        file.write(row_str)
        file.close()

        sleep(TIME_BETWEEN_READINGS)


if __name__ == "__main__":
    # execute only if run as a script
    main()
