#!/usr/bin/env python3

import numpy as np
import time


black = (0, 0, 0)
blue = (0, 0, 220)
green = (0, 180, 0)
grey = (24, 20, 20)
lime = (110, 200, 0)
magenta = (200, 0, 25)
orange = (255, 60, 0)
pink = (255, 0, 180)
red = (230, 0, 0)
skyblue = (0, 240, 240)
turquoise = (0, 240, 45)
violet = (80, 0, 200)
white = (255, 255, 230)
yellow = (250, 230, 0)


# draw a full row
def row(ml, y, color = blue, show = True):
    for x in range(ml.width):
        ml.set_pixel(x, y, color[0], color[1], color[2])
    if show == True:
        ml.show()

# draw a full row
def col(ml, x, color = blue, show = True):
    for y in range(ml.height):
        ml.set_pixel(x, y, color[0], color[1], color[2])
    if show == True:
        ml.show()


# draw a rect
def rect(ml, x1, x2, y1, y2, color = blue, show = True):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            ml.set_pixel(x, y, color[0], color[1], color[2])
    if show == True:
        ml.show()


# draw a line with defined start and endpoint
def Line(ml, x1, x2, y1, y2, color=blue, show = True):
    dx = abs(x2-x1)
    dy = abs(y2-y1)

    r = np.sqrt(dx**2 + dy**2)
    alpha = np.arcsin(dx/r)

    polarLine(ml,x1,y1,int(r),alpha,color)

    if show == True:
        ml.show()

# draw a point in polar coordinates
def polarPoint(ml, x, y, r, alpha, color = blue, show = True):

    x1=x
    y1=y

    # draw center point
    #ml.set_pixel(x1, y1, *color)

    x2 = x1 + r * np.sin(alpha)
    y2 = y1 + r * np.cos(alpha)

    x2 = int(np.round(x2))
    y2 = int(np.round(y2))

    # draw radius point
    ml.set_pixel(int(x2), int(y2), *color)

    if show == True:
        ml.show()


# draw a point in polar coordinates
def polarLine(ml,x,y, r, alpha, color=blue,show=True):
    LinePoints =  2 * r
    dr = 1/LinePoints

    for i in range (LinePoints):

        x2 = x + i * dr * r * np.sin(alpha)
        y2 = y + i * dr * r * np.cos(alpha)

        x2 = int(np.round(x2))
        y2 = int(np.round(y2))

        # draw radius point
        ml.set_pixel(int(x2), int(y2), *color)

    if show == True:
        ml.show()



def circle_unfilled(ml, mx,my, r, alpha=0, color=blue, delay=0, show=True):

    deg = np.pi / 18
    steps = 2 * np.pi / deg

    for step in range(int(steps)):
        polarPoint(ml,mx,my,r,step*deg,color, show=False)
        time.sleep(delay)

    if show == True:
        ml.show()



def circle_filled(ml, mx,my, r, alpha=0, color=blue, delay=0, show=True):

    deg = np.pi / 18
    steps = 2 * np.pi / deg

    for step in range(int(steps)):
        polarLine(ml,mx,my,r,step*deg,color,show=False)
        time.sleep(delay)
        if delay:
            ml.show

    if show == True:
        ml.show()
