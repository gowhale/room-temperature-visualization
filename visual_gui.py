import pygame
import sys
from pygame.locals import *
import time
from random import randrange
from colour import Color
red = Color("red")
colors = list(red.range_to(Color("blue"),101))
print(colors)

def interpolate_colours (colour1, colour2, percentage):
    differnce_in_red = colour1[0] - colour2[0]
    differnce_in_green = colour1[1] - colour2[1]
    differnce_in_blue = colour1[2] - colour2[2]

    current_red = colour1[0] - int(differnce_in_red/100*percentage)
    current_green = colour1[1] - int(differnce_in_green/100*percentage)
    current_blue = colour1[2] - int(differnce_in_blue/100*percentage)

    return (current_red, current_green, current_blue)


def main():
    pygame.init()

    house_top_corner = {"x": 200, "y": 150}
    house_dimensions = {"height": 100, "width": 100}

    DISPLAY = pygame.display.set_mode((500, 400), 0, 32)

    WHITE = (255, 255, 255)

    RED = (255,0,0)
    GREEN = (0,255,0)

    DISPLAY.fill(WHITE)
    count = 1
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        count = (count + 1) % 100
        pygame.display.update()
        random_colour = (randrange(250), randrange(250), randrange(250))
        random_colour = (randrange(250), randrange(250), randrange(250))
        square_coordinates = (
            house_top_corner["x"], house_top_corner["y"], house_dimensions["width"], house_dimensions["height"])
        pygame.draw.rect(
            DISPLAY, random_colour, square_coordinates)
        polygon_coordinates = [[house_top_corner["x"], house_top_corner["y"]], [house_top_corner["x"] + int(house_dimensions["width"]/2), house_top_corner["y"] - int(
            house_dimensions["height"]/2)], [house_top_corner["x"] + house_dimensions["width"], house_top_corner["y"]]]
        interpolated_colour = (int(colors[count].get_red()*255),int(colors[count].get_green()*255),int(colors[count].get_blue()*255))
        print(interpolated_colour)
        pygame.draw.polygon(DISPLAY,interpolated_colour , polygon_coordinates, 0)
        time.sleep(0.1)


main()
