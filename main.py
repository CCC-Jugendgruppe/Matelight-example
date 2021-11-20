import matelight.draw as draw #we need to import the draw.py for the program. We use this here as draw
import ml_simulator.matelight as ml #We need to import the Matelightsimulator for testing. We use this here as ml.
import time #we need to import time for the program
import numpy as np #we also need the package numpy which we use as np


disp = ml.Matelight(3,4) #here the number of mate boxes is defined

disp.set_pixel(2,5,255,0,0) #here a point is set at x2 and at y5. In addition, the color can be changed here, which is blue by default.
disp.show() #this line is necessary for the matelight to output something
time.sleep(10) #this is optional, it serves to make the effect visible for a few seconds