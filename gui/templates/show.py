__author__ = 'perun'


from tkinter import *
import core.distribution as dist
import gui.templates.widgets as tpl


class ShowInfo(Frame):
    def __init__(self, instance, parent=None):
        Frame.__init__(self, parent)
        self.pack(side=TOP)

        self.make_form(self.process_data(instance))

    def process_data(self, instance):
        fields = [(x, instance.__dict__[x]) for x in instance.__dict__.keys()]
        fields.sort()
        return fields

    def make_form(self, fields):
        tpl.label(self, TOP, 'Instance variables')
        for x, y in fields:
            row = Frame(self)
            tpl.label(row, LEFT, x, width=20)
            tmp = StringVar()
            tmp.set(y)
            tpl.entry(row, LEFT, tmp, width=20, state='disabled')
            row.pack(side=TOP, fill=X)

if __name__ == '__main__':
    root = Tk()
    d = dist.Data()
    d.create_package_network(100, 1000, 1000)
    d.create_package_network(50, 500, 500)
    ShowInfo(d.networks[0], root)
    root.mainloop()