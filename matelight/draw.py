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


# draw a line with defined start and endpoint
def Line(ml, x1, x2, y1, y2, color=blue, show = True):
    Dx = abs(x2-x1)+1       # Delta x (komplette x-Länge)
    Dy = abs(y2-y1)+1       # Delta y (komplette y-Länge)

    # Ermittlung der Steigung: 1 positiv; -1 negativ
    if (x2 < x1 and y2 > y1) or (x2 > x1 and y2 < y1):
        direction = -1
    else:
        direction = 1

    # Sollte Delta x größer sein als Delta y, wird eine Iteration über x durchgeführt, sonst über y (45° Regel)
    if Dx > Dy:

        # Fehler abfangen: Es soll nur von links nach rechts gezeichnet werden
        if x1 < x2:
            xa = x1
            ya = y1
            xb = x2
            yb = y2
        else:
            xa = x2
            ya = y2
            xb = x1
            yb = y1

        dy = direction * Dy / Dx                            # y-Wert, der pro Pixel in x-Richtung addiert werden muss
        sum_y = 0                                           # die dy-Werte werden schrittweise aufsummiert

        for x in range(Dx-1):
            sum_y = sum_y + dy                              # Summieren der dy-Werte
            y = int(sum_y)                                  # Abschneiden der Nachkommastelle → y-Koordinate
            ml.set_pixel(x+xa,y+ya, *color)                 # Pixel wird gezeichnet

    # falls Delta y größer ist als Delta x, wird eine Iterration über y durchgeführt
    else:
        # Fehler abfangen: Es soll nur von Oben nach Unten gezeichnet werden
        if y1 < y2:
            xa = x1
            ya = y1
            xb = x2
            yb = y2
        else:
            xa = x2
            ya = y2
            xb = x1
            yb = y1

        dx = direction * Dx / Dy                            # x-Wert, der pro Pixel in y-Richtung addiert werden muss
        sum_x = 0                                           # die dx-Werte werden schrittweise aufsummiert

        for y in range(Dy-1):
            sum_x = sum_x + dx                              # Summieren der dx-Werte
            x = int(sum_x)                                  # Abschneiden der Nachkommastelle → x-Koordinate
            ml.set_pixel(x+xa,y+ya, *color)                 # Pixel wird gezeichnet

    ml.set_pixel(xb,yb, *color)                             # Letzten Pixel zeichnen (muss separat gezeichnet werden, da sonst ein Pixel zu weit)

    if show == True:
        ml.show()                                               # Anzeigen der Zeichnung auf dem MateLight




# draw a point in polar coordinates
def polarLine(ml,x,y, r, alpha, color=blue,show=True):
    LinePoints =  2 * r
    dr = 1/LinePoints

    x2 = int(round((r * np.cos(alpha) + x),0))
    y2 = int(round((r * np.sin(alpha) + y),0))

    Line(ml,x,x2,y,y2,color,show)



def circle_unfilled(ml, mx,my, r, alpha=0, color=blue, delay=0, show=True):

    deg = np.pi / 18
    steps = 2 * np.pi / deg

    for step in range(int(steps)):
        polarPoint(ml,mx,my,r,step*deg,color, show=False)
        time.sleep(delay)
        if delay:
            ml.show()

    if show == True:
        ml.show()



def circle_filled(ml, mx,my, r, alpha=0, color=blue, delay=0, show=True):

    deg = np.pi / 18
    steps = 2 * np.pi / deg

    for step in range(int(steps)):
        polarLine(ml,mx,my,r,step*deg,color,show=False)
        time.sleep(delay)
        if delay:
            ml.show()

    if show == True:
        ml.show()
