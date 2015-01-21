__author__ = 'perun'


from tkinter import *
import core.distribution as dist
import gui.templates.widgets as tpl
import sys


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
            tpl.label(row, LEFT, x, width=28)
            tmp = StringVar()
            tmp.set(y)
            tpl.entry(row, LEFT, tmp, width=20, state='disabled')
            row.pack(side=TOP, fill=X)


class ShowPathsThroughLink(Frame):
    def __init__(self, parent, paths):
        Frame.__init__(self, parent)
        self.pack(side=TOP)
        self.parent = parent
        self.make_form(paths)

    def make_form(self, paths):
        for path in paths:
            row = Frame(self)
            row.pack(side=TOP)
            Label(row, text=path+' [b/s]').pack(side=LEFT)
            tmp = StringVar()
            tmp.set(paths[path])
            Entry(row, textvariable=tmp, state='disabled').pack(side=LEFT)

        row = Frame(self)
        row.pack(side=TOP)
        Button(row, text='Close', command=self.parent.destroy).pack(side=TOP)




class LogBox(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)

        self.parent = parent
        self.text_box = None
        self.disable_pressed = False

        self.make_box()

    def make_box(self):
        row1 = Frame(self)
        row1.pack(side=TOP)
        sbar = Scrollbar(row1)
        self.text_box = Text(row1, relief=SUNKEN)
        sbar.config(command=self.text_box.yview)
        self.text_box.config(yscrollcommand=sbar.set, height=15)
        sbar.pack(side=RIGHT, fill=Y)
        self.text_box.pack(side=LEFT, expand=YES, fill=BOTH)
        row = Frame(self)
        row.pack(side=BOTTOM)
        Button(row, text='Clear', command=self.clear_text).pack(side=LEFT, padx=5, pady=5)
        sys.stdout = RedirectStdout(self.text_box)

    def clear_text(self):
        #print('lala')
        self.text_box.config(state='normal')
        self.text_box.delete('1.0', END)
        self.text_box.config(state='disabled')


class RedirectStdout(object):
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, string):
        self.text_widget.config(state='normal')
        self.text_widget.insert('end', string)
        self.text_widget.see('end')
        self.text_widget.config(state='disabled')


if __name__ == '__main__':
    root = Tk()
    d = dist.Data()
    d.create_package_network(100, 1000, 1000)
    d.create_package_network(50, 500, 500)
    #ShowInfo(d.networks[0], root)
    LogBox(root)
    for x in range(30):
        print('IKSO')
    root.mainloop()