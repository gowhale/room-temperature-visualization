import pygame
import sys
from pygame.locals import *
import time
from random import randrange


def main():
    pygame.init()

    house_top_corner = {"x": 200, "y": 150}
    house_dimensions = {"height": 100, "width": 100}

    DISPLAY = pygame.display.set_mode((500, 400), 0, 32)

    WHITE = (255, 255, 255)

    DISPLAY.fill(WHITE)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        random_colour = (randrange(250), randrange(250), randrange(250))
        pygame.draw.rect(
            DISPLAY, random_colour, (house_top_corner["x"], house_top_corner["y"], house_dimensions["width"], house_dimensions["height"]))
        pygame.draw.polygon(DISPLAY, random_colour, [[house_top_corner["x"], house_top_corner["y"]], [
                            house_top_corner["x"] + int(house_dimensions["width"]/2), house_top_corner["y"] - int(house_dimensions["height"]/2)], [house_top_corner["x"] + house_dimensions["width"], house_top_corner["y"]]], 0)
        time.sleep(1)


main()
