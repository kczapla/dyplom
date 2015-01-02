__author__ = 'perun'

from tkinter import *
from tkinter.messagebox import *

import core.distribution as distribution
import gui.templates.quitter as quitter
import gui.templates.widgets as tpl
import gui.windows.popups as popups


class Menu(Frame):
    def __init__(self, distribution, parent=None, **extras):
        Frame.__init__(self, parent, **extras)
        self.pack(side=TOP, **extras)

        self.distribution = distribution

        self.make_content()

    def make_content(self):
        tpl.label(self, TOP, 'MENU')
        tpl.button(self, TOP, 'Create network', lambda: popups.ChooseNetwork(self.distribution,
                                                                             Toplevel(self))).pack(padx=5)
        tpl.button(self, TOP, 'Create interest matrix', self.chose_interest_matrix).pack(padx=5)
        tpl.button(self, TOP, 'Show data', self.show_data).pack(padx=5)
        quitter.Quitter(self)

    def chose_interest_matrix(self):
        if self.distribution.index_networks:
            popups.CreateInterestMatrix(self.distribution,
                                        Toplevel(self))
        else:
            showwarning('Warning', 'Networks don\'t exist. Create networks first to use this option.')

    def delete_network(self):
        if self.distribution.index_networks:
            pass

    def show_data(self):
        if self.distribution.index_networks:
            popups.ShowData(self.distribution, Toplevel())
        else:
            showwarning('Warning', 'Networks don\'t exist. Create networks first to use this option.')


if __name__ == '__main__':

    root = Tk()
    d = distribution.Data()
    for x in range(6):
        d.create_package_network('ikso' + str(x), 100, 1000, 1000)
        d.create_circuit_network('lolo' + str(x), 50, 500)
    m = Menu(d, root)
    m.pack()
    root.mainloop()