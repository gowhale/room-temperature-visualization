import datetime
import csv


class ReadingsLog ():
    """This class represents how the data is saved to a file"""

    def __init__(self, include_weather):
        """Initialises the creation of a readings log.

        Keyword arguments:
        include_weather -- option weather weather api will be used
        """

        # Create Headers
        headers = [["Time", "Sensor Temperature",
                    "Sensor Humidity", "Sensor Pressure"]]
        if (include_weather):
            headers[0].append("Weather Forecast Temperature")
            headers[0].append("Weather Forecast Description")

        # Create File
        current_datetime = datetime.datetime.now()
        pretty_date = (current_datetime.strftime("%Y:%m:%d"))
        pretty_time = (current_datetime.strftime("%H:%M:%S"))
        file_name = ("reports/temperature-report-{}-{}.csv").format(pretty_date,
                                                                    pretty_time)

        with open(file_name, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(headers)

        self.file_name = file_name

    def append_row(self, row):
        """Add a row onto the end of the current log

        Keyword arguments:
        row -- [list] containing seperated cells
        """
        print(row)
        file = open(self.file_name, 'a')
        row_str = ",".join(row)+"\n"
        file.write(row_str)
        file.close()
