from bme280 import readBME280ID
from bme280 import readBME280All


class Sensor ():

    def __init__(self):
        (chip_id, chip_version) = readBME280ID()
        print("Chip ID     :", chip_id)
        self.chip_id = chip_id
        self.chip_version = chip_version

        temperature, pressure, humidity = readBME280All()

        self.temperature = temperature
        self.pressure = pressure
        self.humidity = humidity

    def get_temperature(self):
        temperature, _, _ = readBME280All()
        return temperature

    def get_humidity(self):
        _, humidity, _ = readBME280All()
        return humidity

    def get_pressure(self):
        _, _, pressure = readBME280All()
        return pressure
