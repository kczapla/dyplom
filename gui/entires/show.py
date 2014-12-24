__author__ = 'perun'


from tkinter import *
import gui.templates.scrolled_list as scl


class ShowAccess(Frame):
    def __init__(self, distribution, parent=None):
        Frame.__init__(self, parent)
        self.distribution = distribution


    def make_form(self):
        pass