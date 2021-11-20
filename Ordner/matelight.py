#!/usr/bin/env python3

from apa102_pi.driver import apa102
import numpy as np

class Matelight():
    """
    Very small library to simplify creating effects for our matelight.

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

    def __init__(self, crates_horizontal = 1, crates_vertical = 1, serial="none", brightness=4):
        """Create a new Matelight with the given number of crates."""
        if crates_horizontal < 1 or crates_vertical < 1:
            raise ValueError("crates_horizontal and crates_vertical have to be larger than 0!")
#        if crates_vertical % 2 == 0 and crates_horizontal > 1:
#            raise ValueError("crates_vertical has to be odd, if crates_horizontal is larger than 1!")
        self.width = crates_horizontal * 5
        self.height = crates_vertical * 4
        self.num_leds = self.width * self.height
        #self.strip = apa102.APA102(num_led = self.num_leds + 1, serial = serial, global_brightness=10)
        self.strip = apa102.APA102(num_led = self.num_leds + 1, mosi=10, sclk=11)
        self.strip.global_brightness = brightness
        self.create_lookup_table(crates_horizontal, crates_vertical)

    def create_lookup_table(self, w, h):
        """Helper function to create mapping between x/y ccordinates and led ids"""
        self.lut = [[0] * self.height for x in range(self.width)]
        for x in range(self.width):
            for y in range(self.height):
                ch = x // 5
                cv = y // 4
                # crate base value
                if ch % 2 == 0: # even crate columns
                    i = ((ch + 1) * h - cv - 1) * 20
                else:           # odd crate columns
                    i = (ch * h + cv) * 20
                # column value inside the crate
                if cv % 2 == 0: # left to right crates
                    i += (x % 5) * 4
                else:           # right to left crates
                    i += 16 - (x % 5) * 4
                # individual values inside each column of four bottles
                if x % 2 == 0:  # bottom up
                    i += 3 - (y % 4)
                else:           # top down
                    i += (y % 4)
                self.lut[x][y] = i

        if (self.height%2 == 0):
            self.lut = np.flip(self.lut,0)

    def __del__(self):
        self.strip.cleanup()

    def pretty_print_lut(self):
        """Function to show lookup table in a nice format for debugging"""
        ch = self.width // 5
        cv = self.height // 4
        sep = "+" + ("-" * 20 + "+") * ch
        print(sep)
        for y in range(cv):
            for i in range(4):
                for x in range(ch):
                    print("|", end="")
                    for k in range(5):
                        print("{:^4}".format(self.lut[x*5+k][(y*4+i)]), end="")
                print("|")
            print(sep)


    def set_pixel(self, x, y, r, g, b):
        """
        Set the pixel at position x/y to the color specified by the last three arguments.

        This will not be visible immediately, you have to call show() for that.
        Both x and y are zero-based and start in the top-left corner.
        The r/g/b values should be in range [0-255]
        """
        # TODO: assert that coordinates are valid?
        self.strip.set_pixel(self.lut[x][y], r, g, b)

    def clear(self, show=True):
        # clear all pixels
        for y in range(self.height):
            for x in range(self.width):
                self.set_pixel(x,y,0,0,0)

        # directly show on MateLight?
        if show==True:
            self.show()


    def show(self):
        """Actually show everything."""
        self.strip.show()

if __name__ == "__main__": 
    # initialize the library and the strip
    ml = Matelight(1, 1)

    # set each led once to show correct ordering
    for x in range(ml.width):
        for y in range(ml.height):
            print(x,y)
            ml.clear()
            ml.set_pixel(x, y, 255, 0, 0)
            ml.show()
