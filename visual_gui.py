import pygame
import sys
from pygame.locals import QUIT
import time
from random import randrange
from colours import ColourScale
from weather_api import get_weather
import datetime
from sensor import Sensor

# def draw_scale():


def text_objects(text, font):
    text_surface = font.render(text, True, (0, 0, 0))
    return text_surface, text_surface.get_rect()


def get_current_ss():
    return (datetime.datetime.now().strftime("%S"))


def get_current_hh():
    return (datetime.datetime.now().strftime("%M"))


def main():
    pygame.init()

    DISPLAY = pygame.display.set_mode((500, 400), 0, 32)
    pygame.display.set_caption("temperature Analysis") 
    WHITE = (255, 255, 255)
    DISPLAY.fill(WHITE)

    house_top_corner = {"x": 200, "y": 150}
    house_dimensions = {"height": 100, "width": 100}

    colour_scale = ColourScale("blue", "red", 100)
    colour_scale.set_max_temp(30)
    colour_scale.set_min_temp(0)

    print(colour_scale.get_colours())

    scale_locations = {"x": 50, "y": 50}
    scale_dimensions = {"height": 10, "width": 10}

    for part in range(1, 31):
        current_colour = colour_scale.get_temperature_colours_pigame_format(
            part)

        scale_coordinates = (
            scale_locations["x"], scale_locations["y"]+(part*scale_dimensions["height"]), scale_dimensions["width"], scale_dimensions["height"])
        pygame.draw.rect(
            DISPLAY, current_colour, scale_coordinates)

        scale_text = pygame.font.Font('freesansbold.ttf', 10)
        current_temp = part - 1
        text = "{}C".format(current_temp)
        text_surface, text_rect = text_objects(text, scale_text)
        text_rect.center = (
            scale_locations["x"]-15, scale_locations["y"]+(part*scale_dimensions["height"]) + 5)
        DISPLAY.blit(text_surface, text_rect)

    temp = 1
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        if(get_current_ss() == "00"):
            # if(int(get_current_hh()) % 5 == 00):


            enviroment_sensor = Sensor()
            temp = enviroment_sensor.get_temperature()
            print("TEMP IS: {}".format(temp))
            print(temp)

            pygame.display.update()

            # Creates the square part of the house
            square_coordinates = (
                house_top_corner["x"], house_top_corner["y"], house_dimensions["width"], house_dimensions["height"])
            current_colour = colour_scale.get_temperature_colours_pigame_format(
                temp)
            pygame.draw.rect(
                DISPLAY, current_colour, square_coordinates)

            # Creates the top of the house
            polygon_coordinates = [[house_top_corner["x"], house_top_corner["y"]], [house_top_corner["x"] + int(house_dimensions["width"]/2), house_top_corner["y"] - int(
                house_dimensions["height"]/2)], [house_top_corner["x"] + house_dimensions["width"], house_top_corner["y"]]]
            print(current_colour)
            pygame.draw.polygon(DISPLAY, current_colour,
                                polygon_coordinates, 0)

            # Creates the circle around the house simulating weather
            circle_location = {"x": int(house_top_corner["x"] + house_dimensions["width"]/2), "y": int(
                house_top_corner["y"] + house_dimensions["height"]/3)}
            # enviroment_temperature = (float(get_weather("Cardiff")))
            enviroment_temperature = temp #To stop too many API calls
            print("ENVIROMENT TEMP: {}".format(enviroment_temperature))

            enviroment_colour = colour_scale.get_temperature_colours_pigame_format(
                enviroment_temperature)

            pygame.draw.circle(DISPLAY, enviroment_colour, (circle_location["x"], circle_location["y"]), int(
                house_dimensions["height"]*1.5), 10)

            # Waits for 1 second so that the API is only called once
            time.sleep(1)


main()
