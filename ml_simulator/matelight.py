#!/usr/bin/env python3

import argparse

from ml_simulator import gui
from ml_simulator.fileio import savefile

class Matelight():
    """
    Very small library to simulate our matelight effects.
    Replace this file with the other matelight.py
    Beware to make a copy of the original matelight.py before copying!

    Basic usage:
        from matelight import Matelight
        ml = Matelight()
        for x in range(ml.width):
            for y in range(ml.height):
                ml.clear()
                ml.set_pixel(x, y, 255, 0, 0)
                ml.show()

    Orientation of the crates (bottom left crate for example):
             +---------------+
             |(o)(o)(o)(o)(o)| <- output
             |(o)(o)(o)(o)(o)|
             |(o)(o)(o)(o)(o)|
    input -> |(o)(o)(o)(o)(o)|
             +---------------+
    """

    def __init__(self, crates_horizontal=1, crates_vertical=1, serial="window/canvas"):
        """Create a new Matelight with the given number of crates and outputs in given format to serial."""
        if crates_horizontal < 1 or crates_vertical < 1:
            raise ValueError("crates_horizontal and crates_vertical have to be larger than 0!")
        self.width = crates_horizontal * 5
        self.height = crates_vertical * 4
        self.num_leds = self.width * self.height
        self.leds = [[[0,0,0] for y in range(self.height)] for x in range(self.width)]
        self.diff = []

        self.serials = []
        if "terminal/debug" in serial:
            self.serials.append("terminal/debug")
        if "window/canvas" in serial:
            self.serials.append("window/canvas")
            self.simulator = gui.Gui(self.width, self.height)
        if "file/json" in serial:
            self.serials.append("file/json")
            filename = ""
            serials = serial.split()
            for s in serials:
                if s.startswith("file/json"):
                    filename = s.split(":")[1]
                    break
            self.filename = filename if filename else "output.json"
            self.difftrack = []
        if not self.serials:
            print("Warning: no serial given. Using terminal/debug")
            self.serials.append("terminal/debug")


    def set_pixel(self, x, y, r, g, b):
        """
        Set the pixel at position x/y to the color specified by the last three arguments.
        
        This will not be visible immediately, you have to call show() for that.
        Both x and y are zero-based and start in the top-left corner.
        The r/g/b values should be in range [0-255]
        """
        self.diff.append([(x,y), (r,g,b)])

    def clear(self, show=True):
        """Clear the whole display."""
        self.diff.clear()
        for y in range(self.height):
            for x in range(self.width):
                self.leds[x][y][0] = 0;
                self.leds[x][y][1] = 0;
                self.leds[x][y][2] = 0;

        # directly show on MateLight?
        if show==True:
            self.show()

    def show(self):
        """Actually show everything."""
        if not self.diff:
            return
        for d in self.diff:
            self.leds[ d[0][0] ][ d[0][1] ][ 0 ] = d[1][ 0 ]
            self.leds[ d[0][0] ][ d[0][1] ][ 1 ] = d[1][ 1 ]
            self.leds[ d[0][0] ][ d[0][1] ][ 2 ] = d[1][ 2 ]
        if "terminal/debug" in self.serials:
            for y in range(self.height):
                for x in range(self.width):
                    print(f"{x}/{y}:", *self.leds[x][y])
        if "window/canvas" in self.serials:
            for y in range(self.height):
                for x in range(self.width):
                    self.simulator.set_bottle_color(x, y, *self.leds[x][y])
            self.simulator.update()
        if "file/json" in self.serials:
            # todo check time diff
            timepassed = 23
            self.difftrack.append({
                'time': timepassed,
                'colors': []
                })
            for d in self.diff:
                self.difftrack[-1]['colors'].append({
                    'x': d[0][0],
                    'y': d[0][1],
                    'r': d[1][0],
                    'g': d[1][1],
                    'b': d[1][2],
                    })
            savefile(self.filename, difftrack=self.difftrack)
        self.diff.clear()


if __name__ == "__main__": 
    # initialize the library and the strip
    # ml = Matelight(1, 1, "window/canvas")
    ml = Matelight(1, 1, "window/canvas terminal/debug")

    # set each led once to show correct ordering
    for x in range(ml.width):
        for y in range(ml.height):
            print(x,y)
            ml.clear()
            ml.set_pixel(x, y, 255, 0, 0)
            ml.show()
