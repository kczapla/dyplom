__author__ = 'perun'

from tkinter import *


class ScrolledList(Frame):
    def __init__(self, options, parent=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)

        self.listbox = Listbox(None)

        self.make_widgets(options)

    def handle_list_left(self, event):
        """
        Methods services left click of mouse.
        :param event: Mouse event.
        """
        index = self.listbox.curselection()
        label = self.listbox.get(index)
        self.run_command_left(label)

    def run_command_left(self, selection):
        """
        Left mouse button callback
        :param selection: Label of chose item in listbox
        """
        print('You selected: ', selection)

    def handle_list_right(self, event):
        """
        Methods services right click of mouse.
        :param event: Mouse event.
        """
        if self.listbox.curselection():
            index = self.listbox.curselection()
            self.listbox.select_clear(index)
        xy = event.x, event.y
        index = self.listbox.nearest(event.y)
        self.listbox.select_set(index)
        self.listbox.activate(index)
        label = self.listbox.get(index)

        self.run_command_right(label, xy)

    def run_command_right(self, selection, xy):
        """
        Right mouse button callback
        :param selection: Label of chose item in listbox
        """
        print('You selected: ', selection, 'on position: ', xy)

    def make_widgets(self, options):
        """
        Method creates listbox and bind left and right click mouse events
        :param options: name of list objects
        """
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
        list.bind('<Double-1>', self.handle_list_left)
        list.bind('<Button-3>', self.handle_list_right)
        self.listbox = list

    def delete_selected_item_from_listbox(self, selection):
        """
        Deletes selected item from list box
        :param selection: selected item
        """
        index = self.listbox.curselection()

        self.listbox.delete(index)
        print('Item {} deleted from list successfully.'.format(index))


if __name__ == '__main__':
    option = (('Lumberjack-%s' % x) for x in range(20))  # or map/lambda, [...]
    ScrolledList(option).mainloop()