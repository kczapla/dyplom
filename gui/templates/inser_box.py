__author__ = 'perun'


import gui.templates.widgets as tpl
import core.distribution
import core.networks
import gui.config.insert_box as conf_popups
from tkinter import *
from tkinter.messagebox import *


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
        circuit_entry_fields = 'Name', 'Voice latency [Erl]', 'Loss'
        package_entry_fields = 'Name', 'Voice latency [Pack/s]', 'Video latency [Pack/s]', 'BE latency [Pack/s]'

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
        tpl.label(self, TOP, 'Set parameters')
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
            if not entry.get().replace('.', '', 1).isdigit():
                values.append(str(entry.get()))
            else:
                values.append(float(entry.get()))
        if type(values[1]) is float and type(values[2]) is float:
            self.distribution.create_circuit_network(values[0], values[1], values[2])
            self.parent.destroy()
        else:
            showerror('Error', 'Wrong value! Try again!')


class CreateNetworkPackage(CreateNetwork):
    def fetch(self):
        values = []
        for entry in self.entries:
            print('Input => "{}"'.format(entry.get()))
            if not entry.get().replace('.', '', 1).isdigit():
                values.append(str(entry.get()))
            else:
                values.append(float(entry.get()))
        if type(values[1]) is float and type(values[2]) is float and type(values[3]) is float:
            self.distribution.create_package_network(values[0], values[1], values[2], values[3])
            self.parent.destroy()
        else:
            showerror('Error', 'Wrong value! Try again!')


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
            if not entry.get().replace('.', '', 1).isdigit():
                values.append(str(entry.get()))
            else:
                values.append(float(entry.get()))

        if type(self.distribution.networks[self.index]) == core.networks.Circuit:
            if type(values[1]) is float and type(values[2]) is float:
                self.distribution.edit_network(name=values[0], index=self.index, intensity_voice=values[1],
                                               loss=values[2])
                self.parent.destroy()
            else:
                showerror('Error', 'Wrong value! Try again!')
        elif type(self.distribution.networks[self.index]) == core.networks.Package:
            if type(values[1]) is float and type(values[2]) is float and type(values[3]) is float:
                self.distribution.edit_network(name=values[0], index=self.index, intensity_voice=values[1],
                                               intensity_video=values[2],
                                               intensity_be=values[3])
                self.parent.destroy()
            else:
                showerror('Error', 'Wrong value! Try again!')


class CreateNodeEdge(CreateNetwork):
    def fetch(self):
        print('CreateNodeEdge fetch method.')
        values = []
        for entry in self.entries:
            print('Input => "{}"'.format(entry.get()))
            if not entry.get().isdigit():
                values.append(str(entry.get()))
            else:
                values.append(int(entry.get()))
        if type(values[1]) is int and type(values[2]) is int and type(values[3]) is int:
            self.distribution.create_node_edge(values[0], values[1], values[2], values[3])
            self.parent.destroy()
        else:
            showerror('Error', 'Wrong value! Try again!')


class CreateNodeCore(CreateNetwork):
    def fetch(self):
        print('CreateNodeCore fetch method.')
        values = []
        for entry in self.entries:
            print('Input => "{}"'.format(entry.get()))
            if not entry.get().isdigit():
                values.append(str(entry.get()))
            else:
                values.append(int(entry.get()))
        if type(values[1]) is int and type(values[2]) is int and type(values[3]) is int:
            self.distribution.create_node_core(values[0], values[1], values[2], values[3])
            self.parent.destroy()
        else:
            showerror('Error', 'Wrong value! Try again!')


class EditNode(CreateNetwork):
    def __init__(self, index, distribution, parent=None, **extras):
        self.index = index
        self.distribution = distribution

        if type(self.distribution.networks[self.index]) == core.networks.Circuit:
            CreateNetwork.__init__(self, distribution, conf_popups.node_insertbox(), parent, **extras)
        elif type(self.distribution.networks[self.index]) == core.networks.Package:
            CreateNetwork.__init__(self, distribution, conf_popups.node_insertbox(), parent, **extras)

    def fetch(self):
        values = []
        for entry in self.entries:
            print('Input => "{}"'.format(entry.get()))
            if not entry.get().isdigit():
                values.append(str(entry.get()))
            else:
                values.append(int(entry.get()))

        if type(values[1]) is int and type(values[2]) is int and type(values[3]) is int:
            self.distribution.edit_node(name=values[0], index=self.index, buffer_voice=values[1],
                                        buffer_video=values[2], buffer_be=values[3])
            self.parent.destroy()
        else:
            showerror('Error', 'Wrong value! Try again!')


if __name__ == '__main__':

    root = Tk()
    d = core.distribution.Data()
    for x in range(20):
        d.create_package_network('ikso' + str(x), 100, 1000, 1000)
        d.create_circuit_network('ikso' + str(x), 50, 500)
    # cn = ChooseNetwork(d, root)
    # cim = CreateInterestMatrix(d, root)
    # shd = ShowData(d, root)
    #circuit_entry_fields = 'Voice latency [Erl]', 'Loss'
    ep = EditNetworkCircuit(1, d, root)

    root.mainloop()