from bme280 import readBME280ID
from bme280 import readBME280All

# NOTE : If you have a different sensor from the bme280 alter this class to take the readings from you different sensor


class Sensor ():
    """This class represents the physical sensor attached to the rasberry pi."""

    def __init__(self):
        """Initialises the class and sets attributes i.e temp, pressure etc"""
        self.read_chip_information()
        self.read_sensor_readings()

    def read_chip_information(self):
        """Reads general info about chip i.e. chip_id and chip_version"""
        self.chip_id, self.chip_version = readBME280ID()

    def read_sensor_readings(self):
        """Reads sensor data such as temp, pressure and humidity"""
        self.temperature, self.pressure, self.humidity = readBME280All()

    def get_temperature(self):
        """Updates value and returns temp"""
        self.read_sensor_readings()
        return self.temperature

    def get_humidity(self):
        """Updates value and returns humidity"""
        self.read_sensor_readings()
        return self.humidity

    def get_pressure(self):
        """Updates value and returns pressure"""
        self.read_sensor_readings()
        return self.pressure
