import datetime
import csv


class ReadingsLog ():

    def __init__(self, include_weather):

        # Create Headers
        headers = [["Time", "Sensor Temperature",
                    "Sensor Humidity", "Sensor Pressure"]]
        if (include_weather):
            headers[0].append("Weather Forecast Temperature")
            headers[0].append("Weather Forecast Description")
        current_datetime = datetime.datetime.now()

        # Create File
        pretty_date = (current_datetime.strftime("%Y:%m:%d"))
        pretty_time = (current_datetime.strftime("%H:%M:%S"))
        file_name = ("reports/temperature-report-{}-{}.csv").format(pretty_date,
                                                                    pretty_time)

        with open(file_name, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(headers)

        self.file_name = file_name

    def append_row(self, row):
        # Append a row onto the end of the log file
        print(row)
        file = open(self.file_name, 'a')
        row_str = ",".join(row)+"\n"
        file.write(row_str)
        file.close()
