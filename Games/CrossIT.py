""" import pygame

import random

# set our screen's width and height
screenWidth, screenHeight = (800, 800)

pygame.init()

pygame.display.set_caption("10 PRINT in Pygame")
screen = pygame.display.set_mode((screenWidth, screenHeight))

running = True

white = (255, 255, 255)
black = (0, 0, 0)

# size of square, in pixels
square = 20

def drawScreen():
    screen.fill(black)
    # Python version of 10 PRINT happens here
    for x in range(0, screenWidth, square):
        for y in range(0, screenHeight, square):
            if random.random() > 0.5:
                pygame.draw.line(screen, white, (x, y), (x + square, y + square))
            else:
                pygame.draw.line(screen, white, (x, y + square), (x + square, y))

while running:
    key = pygame.key.get_pressed()
    # only draw if user presses spacebar
    if key[pygame.K_SPACE]:
        drawScreen()
    # quit if user presses q
    if key[pygame.K_q]:
        exit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # this updates the display
    pygame.display.flip() """


from random import random
from turtle import *

from freegames import line


def draw():
    """Draw maze."""
    color('black')
    width(5)

    for x in range(-200, 200, 40):
        for y in range(-200, 200, 40):
            if random() > 0.5:
                line(x, y, x + 40, y + 40)
            else:
                line(x, y + 40, x + 40, y)

    update()


def tap(x, y):
    """Draw line and dot for screen tap."""
    if abs(x) > 198 or abs(y) > 198:
        up()
    else:
        down()

    width(2)
    color('red')
    goto(x, y)
    dot(4)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
draw()
onscreenclick(tap)
done()