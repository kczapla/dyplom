__author__ = 'perun'


import gui.templates.widgets as tpl
import core.distribution
import core.networks
import gui.config.insert_box as conf_popups
from tkinter import *


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


class EditNetworkCircuit(CreateNetwork):
    def __init__(self, index, distribution, parent=None, **extras):
        self.index = index
        self.distribution = distribution

        if type(self.distribution.networks[self.index]) == core.networks.Circuit:
            CreateNetwork.__init__(self, distribution, conf_popups.access_network_circuit_insertbox(), parent, **extras)
        elif type(self.distribution.networks[self.index]) == core.networks.Package:
            CreateNetwork.__init__(self, distribution, conf_popups.access_network_package_insertbox(), parent, **extras)

    def fetch(self):
        values = []
        for entry in self.entries:
            print('Input => "{}"'.format(entry.get()))
            values.append(float(entry.get()))

        if type(self.distribution.networks[self.index]) == core.networks.Circuit:
            self.distribution.edit_network(index=self.index, intensity_voice=values[0], loss=values[1])
        elif type(self.distribution.networks[self.index]) == core.networks.Package:
            self.distribution.edit_network(index=self.index, intensity_voice=values[0], intensity_video=values[1],
                                           intensity_be=values[2])
        self.parent.destroy()


class EditNetworkPackage(CreateNetwork):
    def __init__(self, index, distribution, entry_fields, parent=None, **extras):
        CreateNetwork.__init__(distribution, entry_fields, parent, **extras)
        self.index = index

    def fetch(self):
        values = []
        for entry in self.entries:
            print('Input => "{}"'.format(entry.get()))
            values.append(float(entry.get()))
        self.distribution.edit_network(index=self.index, intensity_voice=values[0], intensity_video=values[1],
                                       intensity_be=values[2])
        self.parent.destroy()


if __name__ == '__main__':

    root = Tk()
    d = core.distribution.Data()
    for x in range(20):
        d.create_package_network(100, 1000, 1000)
        d.create_circuit_network(50, 500)
    # cn = ChooseNetwork(d, root)
    # cim = CreateInterestMatrix(d, root)
    # shd = ShowData(d, root)
    #circuit_entry_fields = 'Voice latency [Erl]', 'Loss'
    ep = EditNetworkCircuit(1, d, root)

    root.mainloop()