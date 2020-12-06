import pygame
import sys
from pygame.locals import *
import time
from random import randrange
from colours import ColourScale
from weather_api import get_weather

# def draw_scale():


def text_objects(text, font):
    textSurface = font.render(text, True, (0, 0, 0))
    return textSurface, textSurface.get_rect()


def main():
    pygame.init()

    house_top_corner = {"x": 200, "y": 150}
    house_dimensions = {"height": 100, "width": 100}

    DISPLAY = pygame.display.set_mode((500, 400), 0, 32)

    WHITE = (255, 255, 255)

    RED = (255, 0, 0)
    GREEN = (0, 255, 0)

    test = ColourScale("blue", "red", 100)
    test.set_max_temp(30)
    test.set_min_temp(0)

    print(test.get_colours())

    DISPLAY.fill(WHITE)

    scale_locations = {"x": 50, "y": 50}
    scale_dimensions = {"height": 10, "width": 10}

    for part in range(1, 31):
        current_colour = test.get_tempreture_colours_pigame_format(part)

        scale_coordinates = (
            scale_locations["x"], scale_locations["y"]+(part*scale_dimensions["height"]), scale_dimensions["width"], scale_dimensions["height"])
        pygame.draw.rect(
            DISPLAY, current_colour, scale_coordinates)

        largeText = pygame.font.Font('freesansbold.ttf', 10)
        current_temp = part - 1
        text = "{}C".format(current_temp)
        TextSurf, TextRect = text_objects(text, largeText)
        TextRect.center = (
            scale_locations["x"]-15, scale_locations["y"]+(part*scale_dimensions["height"]) + 5)
        DISPLAY.blit(TextSurf, TextRect)

    temp = 1
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()4
                sys.exit()
        temp = (temp + 0.5) % 30
        print("TEMP IS: {}".format(temp))
        print(temp)
        pygame.display.update()
        square_coordinates = (
            house_top_corner["x"], house_top_corner["y"], house_dimensions["width"], house_dimensions["height"])

        current_colour = test.get_tempreture_colours(temp)
        interpolated_colour = (int(current_colour.get_red(
        )*255), int(current_colour.get_green()*255), int(current_colour.get_blue()*255))
        pygame.draw.rect(
            DISPLAY, interpolated_colour, square_coordinates)
        polygon_coordinates = [[house_top_corner["x"], house_top_corner["y"]], [house_top_corner["x"] + int(house_dimensions["width"]/2), house_top_corner["y"] - int(
            house_dimensions["height"]/2)], [house_top_corner["x"] + house_dimensions["width"], house_top_corner["y"]]]
        print(interpolated_colour)
        pygame.draw.polygon(DISPLAY, interpolated_colour,
                            polygon_coordinates, 0)

        circle_location = {"x": int(house_top_corner["x"] + house_dimensions["width"]/2), "y": int(
            house_top_corner["y"] + house_dimensions["height"]/3)}

        enviroment_tempreture = (float(get_weather("Cardiff")))
        print("ENVIROMENT TEMP: {}".format(enviroment_tempreture))
        enviroment_colour = test.get_tempreture_colours_pigame_format(enviroment_tempreture)

        pygame.draw.circle(DISPLAY, enviroment_colour, (circle_location["x"], circle_location["y"]), int(
            house_dimensions["height"]*1.5), 10)

        time.sleep(5)


main()
