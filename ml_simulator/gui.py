#!/usr/bin/env python3

import tkinter as tk
import tkinter.ttk as ttk
from math import floor

DEBUG_LEVEL = 0

class Gui:

    def __init__(self, width=5, height=4, scale=50):
        self.main = tk.Tk()
#        self.logo = tk.PhotoImage(file="logo.png")
#        self.main.wm_iconphoto('-default', self.logo)
        self.main.wm_title("Matelight simulator")
#        self.main.tk_setPalette(
#            background=theme['bg'],
#            foreground=theme['fg'],
#            activeBackground=theme['bg_active'],
#            activeForeground=theme['fg_active']
#        )
        # self.main.tk.call('tk', 'scaling', 7.0)
        self.main.option_add("*font", ("Montserrat", 16, "bold"))
        
        if scale < 1:
            print(f"Error: scale must not be < 1, is {scale}")
            return
        self.scale = scale
        self.canvas_width  = width * scale
        self.canvas_height = height * scale
        self.simulation = tk.Canvas(self.main, width=self.canvas_width, height=self.canvas_height)
        self.simulation.pack()
        self.simulation.create_rectangle(0, 0, self.canvas_width, self.canvas_height, fill="#000000")
        self.main.update()

    def set_bottle_color(self, x, y, r, g, b):
        color = "#%02x%02x%02x" % (r,g,b)   # rgb to hex
        self.simulation.create_rectangle(x*self.scale, y*self.scale,
                x*self.scale+self.scale, y*self.scale+self.scale,
                fill=color)

    def update(self):
        self.main.update()
        self.main.update_idletasks()

    def close():
        self.main.quit()


if __name__ == "__main__":
    print("not runnable. import this file")
