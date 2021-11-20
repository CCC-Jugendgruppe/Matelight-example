import matelight.draw as draw #we need to import the draw.py for the program, to draw shapes, here as draw.
import ml_simulator.matelight as ml #We need to import the Matelightsimulator for testing. We use this here as ml.
import time # time is needed, to display changes, so the effect doesn't just disappear when done.
import numpy as np # numpy is needed for some math operations.

# here the number of mate boxes is defined. (1 Box is 5x4, so here you get 15x16)
disp = ml.Matelight(3,4) 

"""
Colors are set with the usual (red, green, blue) format, next to the (x, y) coordinates
Alternatively, some colors can be set with words. These are located 
at the top of the 'matelight/draw.py' file
"""
# here a point is set at x2 and at y5. In addition, the color can be changed here, which is blue 
# by default and here set to red.
disp.set_pixel(2,5,255,0,0)

# this line is necessary for the matelight to display changes.
disp.show() 

# this is optional, it serves to make the effect visible for a few seconds
time.sleep(1) 

# clears matelight display
disp.clear()

# You can also draw a full row at once, where the first argument
# is the Matelight-Display, the second the Y-Coordinate and the last
# the color to paint the row in.
draw.row(disp, 3, draw.green)

disp.show()
time.sleep(1)
disp.clear()

# Same as above, except that the 2nd argument provides the X-Coordinate.
draw.col(disp, 4, draw.orange)

disp.show()
time.sleep(1)
disp.clear()


"""
This draws a rectangle with the size of 4x3.
the arguments after the Matelight-Display are 
the 1st x coordinate and the 2nd x coordinate.
Then the 1st y and the 2nd y.
"""
draw.rect(disp, 8, 11, 7, 9, draw.yellow)
disp.show()
time.sleep(1)
disp.clear()

# This draws a point with polar Coordinates.
draw.polarPoint(disp, 7, 3, 3, 4*2*np.pi/36, draw.magenta)
disp.show()
time.sleep(1)
disp.clear()


# Draws a line with defined start- and endpoint, given as x-start, x-end, y-start, y-end.
draw.Line(disp, 14, 10, 14, 7, draw.skyblue)
disp.show()
time.sleep(1)
disp.clear()


# Draws a line with polar coordinates
draw.polarLine(disp, 4, 4, 4, 3*2*np.pi/36, draw.lime)
disp.show()
time.sleep(1)
disp.clear()


# draws a circle that isn't filled with color.
draw.circle_unfilled(disp, 8, 8, 5, draw.violet)
disp.show()
time.sleep(1)
disp.clear()

# draws a circle that is filled with color.
draw.circle_filled(disp, 8, 8, 4, draw.violet)
disp.show()
time.sleep(10)
disp.clear()
