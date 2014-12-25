__author__ = 'perun'

from tkinter import *


class ScrolledList(Frame):
    def __init__(self, options, parent=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)

        self.listbox = Listbox(None)

        self.make_widgets(options)

    def handle_list(self, event):
        index = self.listbox.curselection()
        label = self.listbox.get(index)
        self.run_command(label)

    def run_command(self, selection):
        print('You selected: ', selection)

    def make_widgets(self, options):
        sbar = Scrollbar(self)
        list = Listbox(self, relief=SUNKEN)
        sbar.config(command=list.yview)
        list.config(yscrollcommand=sbar.set)
        sbar.pack(side=RIGHT, fill=Y)
        list.pack(side=LEFT, expand=YES, fill=BOTH)
        pos = 0
        for label in options:
            list.insert(pos, label)
            pos += 1
        # list.config(selectmode=SINGLE, setgrid=1)
        list.bind('<Double-1>', self.handle_list)
        self.listbox = list


if __name__ == '__main__':
    option = (('Lumberjack-%s' % x) for x in range(20))  # or map/lambda, [...]
    ScrolledList(option).mainloop()