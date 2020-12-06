import pygame
import sys
from pygame.locals import *
import time
from random import randrange
from colours import ColourScale


# def draw_scale():

    


def main():
    pygame.init()

    house_top_corner = {"x": 200, "y": 150}
    house_dimensions = {"height": 100, "width": 100}

    DISPLAY = pygame.display.set_mode((500, 400), 0, 32)

    WHITE = (255, 255, 255)

    RED = (255, 0, 0)
    GREEN = (0, 255, 0)

    test = ColourScale("red", "blue", 100)
    test.set_max_temp(30)
    test.set_min_temp(0)

    print(test.get_colours())

    DISPLAY.fill(WHITE)

    scale_locations = {"x": 50, "y": 50}
    scale_dimensions = {"height": 10, "width": 10}

    for part in range (1,30):
        current_colour = test.get_tempreture_colours_pigame_format(part)

        scale_coordinates = (
            scale_locations["x"], scale_locations["y"]+(part*scale_dimensions["height"]), scale_dimensions["width"], scale_dimensions["height"])
        pygame.draw.rect(
            DISPLAY, current_colour, scale_coordinates)

    temp = 1
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
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
        time.sleep(0.1)


main()
