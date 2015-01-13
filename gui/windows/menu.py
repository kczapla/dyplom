__author__ = 'perun'

from tkinter import *
from tkinter.messagebox import *

import core.distribution as distribution
import gui.templates.quitter as quitter
import gui.templates.widgets as tpl
import gui.windows.popups as popups
import gui.templates.show as show


class MenuFrame(Frame):
    def __init__(self, distribution, parent=None, **extras):
        Frame.__init__(self, parent, **extras)
        self.pack(side=TOP, **extras)

        self.parent = parent
        self.distribution = distribution
        self.file_saver = popups.ChooseFile(self.parent)

        self.make_content()

    def make_content(self):

        self.make_top_menu_bar(self.parent)

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

    def make_top_menu_bar(self, win):

        top = Menu(win)

        file = Menu(top)
        file.add_command(label='New...', command=self.new_project, underline=0)
        file.add_command(label='Save as...', command=self.save_file, underline=0)
        file.add_command(label='Open...', command=self.load_file, underline=0)
        file.add_command(label='Exit', command=self.parent.destroy, underline=0)
        top.add_cascade(label='File', menu=file, underline=0)
        win.config(menu=top)

    def not_ready(self):
        showinfo('Info', 'Option is not ready.')

    def save_file(self):
        self.file_saver.save_file(self.distribution)

    def load_file(self):
        self.distribution = self.file_saver.load_file()

    def new_project(self):
        print('Creating new project...')
        self.distribution = distribution.Data()


if __name__ == '__main__':

    root = Tk()
    d = distribution.Data()
    d.test_no_2()
    m = MenuFrame(d, root)

    m.pack()
    root.mainloop()