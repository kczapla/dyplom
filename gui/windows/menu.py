__author__ = 'perun'

from tkinter import *
from tkinter.messagebox import *

import core.distribution as distribution
import gui.templates.quitter as quitter
import gui.templates.widgets as tpl
import gui.windows.popups as popups
import gui.templates.show as show


class Menu(Frame):
    def __init__(self, distribution, parent=None, **extras):
        Frame.__init__(self, parent, **extras)
        self.pack(side=TOP, **extras)

        self.distribution = distribution

        self.make_content()

    def make_content(self):
        menu_box = Frame(self, relief=SUNKEN, bd=1)
        menu_box.pack(side=LEFT, padx=5, pady=5)
        tpl.label(menu_box, TOP, 'MENU')
        tpl.button(menu_box, TOP, 'Create network', lambda: popups.ChooseNetwork(self.distribution,
                                                                                 Toplevel(self))).pack(pady=5, padx=5)
        tpl.button(menu_box, TOP, 'Create node', lambda: popups.ChooseNode(self.distribution,
                                                                           Toplevel(self))).pack(pady=5, padx=5)
        tpl.button(menu_box, TOP, 'Create matrix', self.chose_matrix).pack(pady=5, padx=5)
        tpl.button(menu_box, TOP, 'Show data', self.show_data).pack(pady=5, padx=5)
        tpl.button(menu_box, TOP, 'Process data', self.process_data).pack(pady=5, padx=5)

        quitter.Quitter(menu_box)

        log_box = Frame(self, relief=SUNKEN, bd=1)
        log_box.pack(side=LEFT, padx=5, pady=5)
        show.LogBox(log_box)

    def chose_matrix(self):
        popups.CreateMatrix(self.distribution,
                            Toplevel(self))

    def show_data(self):
        if self.distribution.index_networks:
            popups.ShowData(self.distribution, Toplevel(self))
        else:
            showwarning('Warning', 'Networks don\'t exist. Create networks first to use this option.')

    def process_data(self):
        if self.distribution.index_networks:
            popups.ChooseData(self.distribution, Toplevel(self))
        else:
            showwarning('Warning', 'Networks don\'t exist. Create networks first to use this option.')

    def not_ready(self):
        showinfo('Info', 'Option is not ready.')

if __name__ == '__main__':

    root = Tk()
    d = distribution.Data()
    d.test_no_2()
    m = Menu(d, root)
    m.pack()
    root.mainloop()