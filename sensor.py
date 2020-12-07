from bme280 import readBME280ID
from bme280 import readBME280All

# NOTE : If you have a different sensor from the bme280 alter this class to take the readings from you different sensor


class Sensor ():

    def __init__(self):
        self.read_chip_information()
        self.read_sensor_readings()

    def read_chip_information(self):
        self.chip_id, self.chip_version = readBME280ID()

    def read_sensor_readings(self):
        self.temperature, self.pressure, self.humidity = readBME280All()

    def get_temperature(self):
        self.read_sensor_readings()
        return self.temperature

    def get_humidity(self):
        self.read_sensor_readings()
        return self.humidity

    def get_pressure(self):
        self.read_sensor_readings()
        return self.pressure
