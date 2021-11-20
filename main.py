import matelight.draw as draw #we need to import the draw.py for the program, to draw shapes, here as draw.
import ml_simulator.matelight as ml #We need to import the Matelightsimulator for testing. We use this here as ml.
import time # time is needed, to display changes, so the effect doesn't just disappear when done.
import numpy as np # numpy is needed for some math operations.

#here the number of mate boxes is defined. (1 Box is 5x4, so here you get 15x16)
disp = ml.Matelight(3,4) 

#here a point is set at x2 and at y5. In addition, the color can be changed here, which is blue by default.
disp.set_pixel(2,5,255,0,0)

#this line is necessary for the matelight to display changes.
disp.show() 

#this is optional, it serves to make the effect visible for a few seconds
time.sleep(10) 

# clears matelight display
disp.clear()
