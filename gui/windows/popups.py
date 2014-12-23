__author__ = 'perun'


from tkinter import *
import gui.templates.widgets as tpl
import core.distribution
import gui.entires.getters as getters


class ChooseNetwork(Frame):
    def __init__(self, distribution, parent=None, **extras):
        Frame.__init__(self, parent, **extras)

        self.parent = parent

        self.pack(side=TOP)

        self.distribution = distribution

        self.make_widgets()

        self.focus_set()          # take over input focus,
        self.grab_set()           # disable other windows while I'm open,
        self.wait_window()        # and wait here until win destroyed

    def make_widgets(self):
        circuit_entry_fields = 'Voice latency [Erl]', 'Loss'
        package_entry_fields = 'Voice latency [Pack/s]', 'Video latency [Pack/s]', 'BE latency [Pack/s]'

        tpl.label(self, TOP, 'Create Network')
        tpl.button(self, TOP, 'PSTN/ISDN/GSM', lambda: CreateNetwork(self.distribution, circuit_entry_fields,
                                                                     Toplevel()))
        tpl.button(self, TOP, 'IP', lambda: CreateNetworkPackage(self.distribution, package_entry_fields,
                                                                 Toplevel()))
        tpl.button(self, TOP, 'Quit', self.parent.destroy)


class CreateNetwork(Frame):
    def __init__(self, distribution, entry_fields, parent=None, **extras):
        Frame.__init__(self, parent, **extras)

        self.distribution = distribution
        self.parent = parent
        self.pack(side=TOP)

        self.entry_fields = entry_fields
        self.title = 'Create Network'

        self.entries = []
        self.make_form()
        self.make_buttons()

        self.focus_set()          # take over input focus,
        self.grab_set()           # disable other windows while I'm open,
        self.wait_window()        # and wait here until win destroyed

    def make_form(self):
        tpl.label(self, TOP, 'Set parameters of the network')
        for field in self.entry_fields:
            row = Frame(self)
            lab = Label(row, width=20, text=field)
            ent = Entry(row)
            row.pack(side=TOP, fill=X)
            lab.pack(side=LEFT)
            ent.pack(side=RIGHT, expand=YES, fill=X)
            self.entries.append(ent)

    def make_buttons(self):
        row = Frame(self)
        row.pack(side=TOP, fill=X)
        Button(row, text='Ok', command=self.fetch).pack(side=LEFT, expand=YES, fill=X)
        Button(row, text='Cancel', command=self.parent.destroy).pack(side=RIGHT, expand=YES, fill=X)

    def fetch(self):
        values = []
        for entry in self.entries:
            print('Input => "{}"'.format(entry.get()))
            values.append(float(entry.get()))
        self.distribution.create_circuit_network(values[0], values[1])

        self.parent.destroy()


class CreateNetworkPackage(CreateNetwork):
    def fetch(self):
        values = []
        for entry in self.entries:
            print('Input => "{}"'.format(entry.get()))
            values.append(float(entry.get()))
        self.distribution.create_package_network(values[0], values[1], values[2])
        self.parent.destroy()


class CreateInterestMatrix(Frame):
    def __init__(self, distribution, parent=None, **extras):
        Frame.__init__(self, parent, **extras)
        self.parent = parent
        self.pack(side=TOP)

        self.distribution = distribution

        self.button_names = (('Voice', lambda: getters.MatrixVoiceInterest(self.distribution,
                                                                           'Voice Matrix',
                                                                           Toplevel())),
                            ('Video', lambda: getters.MatrixVideoInterest(self.distribution,
                                                                          'Video Matrix',
                                                                          Toplevel())),
                            ('Best Effort', lambda: getters.MatrixBeInterest(self.distribution,
                                                                             'Voice Matrix',
                                                                             Toplevel())),
                            ('Cancel', self.parent.destroy))
        self.make_form()

    def make_form(self):
        row = Frame(self)
        row.pack(side=TOP)
        Label(row, text='Chose type of traffic').pack(side=TOP)
        for button in self.button_names:
            tpl.button(row, TOP, button[0], button[1])


class ShowData(Frame):
    def __init__(self, distribution, parent=None, **extras):
        Frame.__init__(self, parent, **extras)
        self.parent = parent
        self.pack(side=TOP)

        self.distribution = distribution

    def make_form(self):
        pass


if __name__ == '__main__':

    root = Tk()
    d = core.distribution.Data()
    #cn = ChooseNetwork(d, root)
    cim = CreateInterestMatrix(d, root)

    root.mainloop()