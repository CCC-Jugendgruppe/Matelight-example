#!/usr/bin/env python3

import matelight
import time
import random

rc3_primary_colors = [
        ["#b239ff", "#670295", "#440069", "#240038"],
        ["#6800e7", "#41008b", "#2a005e", "#14002f"],
        ["#05b9ec", "#0076a9", "#025d84", "#002a3a"],
    ]

def hex2rgb(color):
    color = color[1:]
    return tuple(int(color[i:i+2], 16) for i in (0, 2, 4))

def rc3_dots(ml):
    for y in range(ml.height):
        for x in range(ml.width):
            # i = random.randint(len(rc3_primary_colors))
            # color = random.choice(rc3_primary_colors[i])
            color = random.choice(random.choice(rc3_primary_colors))
            ml.set_pixel(x, y, *hex2rgb(color))
    ml.show()
    for _ in range(42):
        x = random.randint(0, ml.width-1)
        y = random.randint(0, ml.height-1)
        color = random.choice(random.choice(rc3_primary_colors))
        ml.set_pixel(x, y, *hex2rgb(color))
        ml.show()
        time.sleep(0.1)


if __name__ == "__main__":
    ml = matelight.Matelight(3, 4, serial="window/canvas")
    ml.clear()

    # while True:
    if True:
        effect = random.randint(1, 9)
        effect = 0
    # for effect in range(6):
        if effect == 0:
            rc3_dots(ml)
        # ml.clear()
