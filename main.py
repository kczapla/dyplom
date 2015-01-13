__author__ = 'perun'


import core.distribution
import gui.windows.menu
from tkinter import *


if __name__ == '__main__':
    root = Tk()
    d = core.distribution.Data()
    m = gui.windows.menu.MenuFrame(d, root)
    m.mainloop()