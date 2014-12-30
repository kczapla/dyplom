__author__ = 'perun'


import gui.templates.show as show
import gui.templates.scrolled_list as scl
import core.distribution as dist
import gui.config.list
import gui.templates.menu_bar as menu_bar
from tkinter import *


class AccessNetworksList(scl.ScrolledList, show.ShowInfo, menu_bar.ContextMenu):
    def __init__(self, distribution, parent=None):
        self.parent = parent
        self.list_frame = Frame(parent)
        self.list_frame.pack(side=LEFT, fill=BOTH, expand=YES)

        self.info_frame = Frame(parent)
        self.info_frame.pack(side=LEFT, fill=BOTH, expand=YES)

        scl.ScrolledList.__init__(self, (network.name for network in distribution.networks),
                                  self.list_frame)

        self.distribution = distribution

    def run_command_left(self, selection):
        """
        When user click two times on item in list, method checks what type of network has been chosen and send it to
        ShowInfo class.
        :param selection: selected item from list (double clicked)
        """
        if 'GSM' in selection:
            for network in self.distribution.networks:
                if selection == network.name:
                    show.ShowInfo.__init__(self, network, self.info_frame)
        elif 'IP' in selection:
            for network in self.distribution.networks:
                if selection == network.name:
                    show.ShowInfo.__init__(self, network, self.info_frame)

    def process_data(self, instance):
        """

        :param instance: Network instance, fetch from cofnig file labels name and values to be displayed in entry.
        :return:
        """
        if 'GSM' in instance.name:
            return gui.config.list.access_network_list_circuit(instance)
        elif 'IP' in instance.name:
            return gui.config.list.access_network_list_package(instance)

    def run_command_right(self, selection, xy):
        tmp = [z + 120 for z in xy]
        xy = tuple(tmp)
        menu_bar.ContextMenu.__init__(self, coordinates=xy, fields=selection, parent=Frame(self.list_frame))

    def make_menu_widget(self, pull_downs, parent):
        self.menu = self.create_top_menu_widget(parent)

        self.create_command(self.menu, 'Edit network', self.not_done)
        self.create_command(self.menu, 'Delete', self.delete_network)

    def delete_network(self):
        index = None
        for network in self.distribution.networks:
            if network.name == self.selection:
                index = network.index
        self.distribution.delete_network(index)
        self.delete_selected_item_from_listbox(self.selection)


if __name__ == '__main__':
    root = Tk()
    d = dist.Data()
    d.create_package_network(100, 1000, 1000)
    d.create_package_network(50, 500, 500)
    d.create_circuit_network(123, 0.02)
    AccessNetworksList(d, root)
    root.mainloop()