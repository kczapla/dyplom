__author__ = 'perun'

from tkinter import *
from tkinter.messagebox import *
import tkinter.filedialog

import gui.templates.widgets as tpl
#import core.distribution
import gui.templates.matrix as matrix
import gui.windows.list as list_box
import gui.templates.inser_box
import gui.config.insert_box
import gui.templates.saver


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
        #circuit_entry_fields = 'Name', 'Voice latency [Erl]', 'Loss'
        circuit_entry_fields = gui.config.insert_box.access_network_circuit_insertbox()
        #package_entry_fields = ('Name', 'Voice latency [Pack/s]', 'Video latency [Pack/s]', 'BE latency [Pack/s]',
                                #'Video package length [kB]', 'Be package length [kB]')
        package_entry_fields = gui.config.insert_box.access_network_package_insertbox()

        tpl.label(self, TOP, 'Create Network')
        tpl.button(self, TOP, 'PSTN/ISDN/GSM', lambda: gui.templates.inser_box.CreateNetwork(self.distribution,
                                                                                             circuit_entry_fields,
                                                                                             Toplevel()))
        tpl.button(self, TOP, 'IP', lambda: gui.templates.inser_box.CreateNetworkPackage(self.distribution,
                                                                                         package_entry_fields,
                                                                                         Toplevel()))
        tpl.button(self, TOP, 'Close', self.parent.destroy)

    def not_ready(self):
        showinfo('Info', 'Option is not ready.')


class ChooseNode(ChooseNetwork):
    def make_widgets(self):
        entry_fields = 'Name', 'Size of voice buffer', 'Size of video buffer', 'Size of be buffer'
        tpl.label(self, TOP, 'Create Node')
        tpl.button(self, TOP, 'Edge', lambda: gui.templates.inser_box.CreateNodeEdge(self.distribution, entry_fields,
                                                                                     Toplevel(self)))
        tpl.button(self, TOP, 'Core', lambda: gui.templates.inser_box.CreateNodeCore(self.distribution, entry_fields,
                                                                                     Toplevel(self)))
        tpl.button(self, TOP, 'Close', self.parent.destroy)


class ChooseData(ChooseNetwork):
    def make_widgets(self):
        tpl.label(self, TOP, 'Process data')
        tpl.button(self, TOP, 'Edge resources', self.calculate_edge_resources)
        tpl.button(self, TOP, 'Flow in the network', self.caculate_flow)
        tpl.button(self, TOP, 'QoS', self.qos)
        tpl.button(self, TOP, 'Quit', self.parent.destroy)

    def calculate_edge_resources(self):
        if not self.distribution.interest_matrix_voice:
            showwarning('Warning!', 'Interest matrix for voice is not initialized. Operation canceled.')
        elif not self.distribution.interest_matrix_video or not self.distribution.interest_matrix_be:
            showwarning('Warning!', 'Interest matrix for video or be is not initialized. Processing data for voice')
            self.distribution.process_data_resources()
            print('Empty video or be interest matrix.')
            showinfo('Done!', 'Resources calculated')
        else:
            self.distribution.process_data_resources()
            print('Calculating resources... Success.')
            showinfo('Done!', 'Resources calculated')

    def caculate_flow(self):
        if not self.distribution.connections:
            showerror('Error', 'Create adjacency matrix first.')
        elif not self.distribution.paths_voice:
            showerror('Error', 'Create paths in the core network.')
        else:
            self.distribution.process_data_flow()
            showinfo('Info', 'Flow in network caaculated...')

    def qos(self):
        if self.distribution.is_flow:
            self.distribution.process_data_qos()
            showinfo('Info', 'QoS parameters calculated...')
        else:
            showerror('Error', 'Calculate traffic flow in the network first.')


class CreateMatrix(Frame):
    def __init__(self, distribution, parent=None, **extras):
        Frame.__init__(self, parent, **extras)
        self.parent = parent
        self.pack(side=TOP)

        self.distribution = distribution

        self.button_names = (('Interest Voice', self.create_voice_matrix),
                            ('Interest Video', self.create_video_matrix),
                            ('Interest Best Effort', self.create_be_matrix),
                            ('Adjacency matrix', self.create_adjacency_matrix),
                            ('Network - Edge router matrix', self.create_net_edge_matrix),
                            ('Paths', self.create_paths_matrix),
                            ('Cancel', self.parent.destroy))
        self.make_form()

    def make_form(self):
        row = Frame(self)
        row.pack(side=TOP)
        Label(row, text='Chose type of traffic').pack(side=TOP)
        for button in self.button_names:
            tpl.button(row, TOP, button[0], button[1])

    def create_net_edge_matrix(self):
        if self.distribution.networks and self.distribution.nodes:
            matrix.NetEdgeMatrix(self.distribution,
                                 2,
                                 'Net - Edge',
                                 Toplevel())
        else:
            showwarning('Warning', 'Networks or nodes don\'t exist. Create networks and nodes \
                                    first to use this option.')

    def create_voice_matrix(self):
        if self.distribution.networks:
            matrix.MatrixVoiceInterest(self.distribution,
                                       self.distribution.index_networks,
                                       'Voice Matrix',
                                       Toplevel())
        else:
            showwarning('Warning', 'Networks don\'t exist. Create networks first to use this option.')

    def create_video_matrix(self):
        if self.distribution.networks:
            matrix.MatrixVideoInterest(self.distribution,
                                       self.distribution.index_networks,
                                       'Voice Matrix',
                                       Toplevel())
        else:
            showwarning('Warning', 'Networks don\'t exist. Create networks first to use this option.')

    def create_be_matrix(self):
        if self.distribution.networks:
            matrix.MatrixBeInterest(self.distribution,
                                    self.distribution.index_networks,
                                    'Voice Matrix',
                                    Toplevel())
        else:
            showwarning('Warning', 'Networks don\'t exist. Create networks first to use this option.')

    def create_adjacency_matrix(self):
        if self.distribution.nodes:
            matrix.MatrixAdjacency(self.distribution,
                                   self.distribution.index_nodes,
                                   'Adjacency Matrix',
                                   Toplevel())
        else:
            showwarning('Warning', 'Nodes don\'t exist. Create networks first to use this option.')

    def create_paths_matrix(self):
        if self.distribution.adjacency_matrix:
            gui.templates.inser_box.CreatePaths(self.distribution, Toplevel())
        else:
            showwarning('Warning', 'Adjacency matrix doesn\'t exist. Create networks first to use this option.')


class ShowData(Frame):
    def __init__(self, distribution, parent=None, **extras):
        Frame.__init__(self, parent, **extras)
        self.parent = parent
        self.pack(side=TOP)

        self.make_form()

        self.distribution = distribution

    def make_form(self):
        tpl.label(self, TOP, 'Chose data to show')
        tpl.button(self, TOP, 'Access networks', lambda: list_box.AccessNetworksList(self.distribution, Toplevel()))
        tpl.button(self, TOP, 'Nodes', lambda: list_box.NodesList(self.distribution, Toplevel()))
        tpl.button(self, TOP, 'Links', lambda: list_box.LinksList(self.distribution, Toplevel()))
        tpl.button(self, TOP, 'Quit', self.parent.destroy)


class ChooseFile(object):
    def __init__(self, parent):
        self.file_opt = options = {}
        options['defaultextension'] = '.txt'
        options['filetypes'] = [('All files', '.*'), ('Text files', '.txt'), ('distribution file', '.dbf')]
        options['parent'] = parent

    def load_file(self):
        self.file_opt['title'] = 'Load file'
        file = tkinter.filedialog.askopenfilename(**self.file_opt)
        #print(file)
        if file:
            return gui.templates.saver.FileSaver().load_object(file)
        else:
            print('File to load not chosen...')

    def save_file(self, instance):
        self.file_opt['title'] = 'Save file'
        file = tkinter.filedialog.asksaveasfilename(**self.file_opt)
        #print(file)
        if file:
            gui.templates.saver.FileSaver().save_object(instance, file)
        else:
            print('File to save not chosen...')


if __name__ == '__main__':

    root = Tk()
    #d = core.distribution.Data()
    #d.create_circuit_network('adam', 123, 0.002, 'g.711')
    #for x in range(20):
    #    d.create_package_network(100, 1000, 1000)
    #    d.create_circuit_network(50, 500)
    # cn = ChooseNetwork(d, root)
    # cim = CreateInterestMatrix(d, root)
    # shd = ShowData(d, root)
    #circuit_entry_fields = 'Voice latency [Erl]', 'Loss'
    #ep = EditNetworkCircuit(1, d, root)
    #ChooseFile(root).save_file(d)
    d = ChooseFile(root).load_file()
    print(d.networks[0].name)

    root.mainloop()
