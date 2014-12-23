__author__ = 'perun'


"""
###############################################################################
wrap up widget construction in functions for easier use, based upon some
assumptions (e.g., expansion); use **extras fkw args for width, font/color,
etc., and repack result manually later to override defaults if needed;
###############################################################################
"""

from tkinter import *


def frame(root=None, side=TOP, **extras):
    """
    Function creates frame for widget
    :param root: Toplevel window
    :param side: side on the screen
    :param extras: additional frame options
    :return: ready widget
    """
    widget = Frame(root)
    widget.pack(side=side, expand=YES, fill=BOTH)
    if extras:
        widget.config(**extras)
    return widget


def label(root, side, text, **extras):
    widget = Label(root, text=text)
    widget.pack(side=side, expand=YES, fill=BOTH)
    if extras:
        widget.config(**extras)
    return widget


def button(root, side, text, command, **extras):
    widget = Button(root, text=text, command=command)
    widget.pack(side=side, expand=YES, fill=BOTH)
    if extras:
        widget.config(**extras)
    return widget


def entry(root, side, linkvar, **extras):
    widget = Entry(root, relief=SUNKEN, textvariable=linkvar)
    widget.pack(side=side, expand=YES, fill=BOTH)
    if extras:
        widget.config(**extras)
    return widget


if __name__ == '__main__':
    root = Tk()
    frm1 = frame(root, TOP)
    frm2 = frame(root, TOP)
    lbl = label(frm1, LEFT, 'test')
    ent_var = StringVar()
    ent = entry(frm1, RIGHT, ent_var)
    btn = button(frm2, LEFT, 'push', lambda: print(ent_var.get()))
    root.mainloop()