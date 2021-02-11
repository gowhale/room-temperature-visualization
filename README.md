# room-temperature-visualization

## 1. Introduction

As it's getting colder now, I wanted to design a system which uses a raspberry pi and a BME280 sensor to read the temperature and then use the openweathermap API to read the temperature.

## 2. Outputs

1. A CSV file containing timestamps and information from openweather API and bme280 sensor. i.e., temperature, pressure, humidity etc. (main.py)
2. A graphical user interface visualising the weather temperature and the temperature of the sensor. (visual_gui.p)

## 3. Prerequisites

1. Raspberry Pi (With OS to run Python)
2. bme280 sensor 
3. installation of all modules found in requirements.txt
4. openweathermap API secret key

## 4. Updates

This repository is still a work in progress.

## 5. Useful resources

1. [Setting up the bme280 sensor](https://www.raspberrypi.org/blog/remote-humidity-detector/)
2. [How to Setup Raspberry Pi Zero WH](https://www.youtube.com/watch?v=3VO4vGlQ1pg)
3. [How to Remote Desktop to Raspberry Pi from Apple Mac](https://www.youtube.com/watch?v=L2XaFmt9xsA)
4. [OpenWeather API](https://openweathermap.org/api)
