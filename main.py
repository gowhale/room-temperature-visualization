import csv
from time import sleep
from random import randrange
import datetime

TIME_BETWEEN_READINGS = 3  # Seconds between readings


def get_temperature():
    # TODO: get tempreture from rasbperry pi sensor rather than just random number
    return (randrange(10))


def get_humidity():
    # TODO: get humidity from rasbperry pi sensor rather than just random number
    return (randrange(10))


def pretty_time(raw_time):
    return (raw_time.strftime("%H:%M:%S"))


def pretty_date(raw_time):
    return (raw_time.strftime("%Y:%m:%d"))


def get_current_time_object():
    currentDT = datetime.datetime.now()

    return currentDT


def create_csv():
    # TODO : Create a new CSV with unique name
    headers = [["time", "temperature", "humidity"]]
    current_datetime = get_current_time_object()
    file_name = ("temperature-report-{}-{}.csv").format(pretty_date(current_datetime),
                                                        pretty_time(current_datetime))
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(headers)

    return file_name


def main():
    # TODO : capture enviroment temp and visualise data
    current_file = create_csv()

    for _ in range(5):
        temperature = get_temperature()
        humidity = get_humidity()
        current_time = get_current_time_object()
        row = [pretty_time(current_time), str(temperature), str(humidity)]
        print(row)
        file = open(current_file, 'a')
        # row_str = [",".join(row)]
        row_str = ",".join(row)+"\n"
        file.write(row_str)
        file.close()

        sleep(TIME_BETWEEN_READINGS)


if __name__ == "__main__":
    # execute only if run as a script
    main()
