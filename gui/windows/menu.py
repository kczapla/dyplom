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
        tpl.button(self, TOP, 'Create node', lambda: popups.ChooseNode(self.distribution,
                                                                       Toplevel(self))).pack(padx=5)
        tpl.button(self, TOP, 'Create matrix', self.chose_matrix).pack(padx=5)
        tpl.button(self, TOP, 'Show data', self.show_data).pack(padx=5)
        tpl.button(self, TOP, 'Process data', self.process_data).pack(padx=5)

        quitter.Quitter(self)

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
    for x in range(6):
        d.create_package_network('ikso' + str(x), 100, 1000, 1000)
        d.create_circuit_network('lolo' + str(x), 50, 500)
    d.create_node_edge('bebebe', 5, 15, 30)
    for abc in range(4):
        d.create_node_core('zzz' + str(abc), 5, 15, 30)
    d.create_node_edge('aeaeaeae', 5, 15, 30)
    m = Menu(d, root)
    m.pack()
    root.mainloop()