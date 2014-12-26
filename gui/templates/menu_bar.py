__author__ = 'perun'


from tkinter import *
from tkinter.messagebox import *


class MenuBar(Frame):
    def __init__(self, fields, parent=None):
        Frame.__init__(self, parent)

        self.parent = parent
        self.make_form(fields)

    def make_form(self, pull_downs):
        top = self.create_top_menu_widget(self.parent)  #Menu(self.parent)
        #self.parent.config(menu=top)

        for main, options in pull_downs:
            tmp1 = Menu(top)
            for option in options:
                self.create_command(tmp1, option, self.not_done, underline=0)
            self.create_cascade(top, tmp1, main, underline=0)

    def create_command(self, pull_down, option, command, **extras):
        pull_down.add_command(label=option, command=command, **extras)

    def create_cascade(self, top, pull_down, name, **extras):
        top.add_cascade(label=name, menu=pull_down, **extras)

    def create_top_menu_widget(self, win):
        top = Menu(win)
        win.config(menu=top)
        return top

    def not_done(self):
        showerror('Not implemented', 'Not yet available')


class ContextMenu(MenuBar):
    def __init__(self, fields, parent=None):
        MenuBar.__init__(self, fields, parent)
        self.pack(side=TOP)

    def make_form(self, pull_downs):
        top = self.create_top_menu_widget(self.parent)
        for main, options in pull_downs:
            tmp1 = Menu(top)
            for name, command in options:
                self.create_command(tmp1, name, command, underline=0)
            self.create_cascade(top, tmp1, main, underline=0)

    def create_top_menu_widget(self, win):
        top = Menu(win)
        return top


def not_done():
    showerror('Not implemented', 'Not yet available')


def make_menu(win):
    top = Menu(win)
    win.config(menu=top)

    file = Menu(top)
    file.add_command(label='New...', command=not_done, underline=0)
    file.add_command(label='Open..', command=not_done, underline=0)
    file.add_command(label='Quit...', command=win.quit, underline=0)
    top.add_cascade(label='File', menu=file, underline=0)

    edit = Menu(top, tearoff=False)
    edit.add_command(label='Cut', command=not_done, underline=0)
    edit.add_command(label='Paste', command=not_done, underline=0)
    edit.add_separator()
    top.add_cascade(label='Edit', menu=edit, underline=0)

    submenu = Menu(top, tearoff=True)
    submenu.add_command(label='Spam', command=win.quit, underline=0)
    submenu.add_command(label='Eggs', command=not_done, underline=0)
    edit.add_cascade(label='Stuff', menu=submenu, underline=0)


if __name__ == '__main__':
    root = Tk()                                        # or Toplevel()
    root.title('menu_win')                             # set window-mgr info
    #fields = (('File', ('New', 'Open', 'Quit')), ('Edit', ('Cut', 'Paste')))
    #fields = ('File', (('New', lambda: print('Ikso')), ('Print', lambda: print('spam'))))
    MenuBar(fields, root)
    #make_menu(root)                                     # associate a menu bar
    msg = Label(root, text='Window menu basics')       # add something below
    msg.pack(expand=YES, fill=BOTH)
    msg.config(relief=SUNKEN, width=40, height=7, bg='beige')
    root.mainloop()