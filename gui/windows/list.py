__author__ = 'perun'


import gui.templates.show as show
import gui.templates.scrolled_list as scl
import core.distribution as dist
import gui.config.list
from tkinter import *


class AccessNetworksList(scl.ScrolledList, show.ShowInfo):
    def __init__(self, distribution, parent=None):
        self.list_frame = Frame(parent)
        self.list_frame.pack(side=LEFT, fill=BOTH, expand=YES)

        self.info_frame = Frame(parent)
        self.info_frame.pack(side=LEFT, fill=BOTH, expand=YES)

        scl.ScrolledList.__init__(self, (network.name for network in distribution.networks), self.list_frame)

        self.distribution = distribution

    def run_command(self, selection):
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

if __name__ == '__main__':
    root = Tk()
    d = dist.Data()
    d.create_package_network(100, 1000, 1000)
    d.create_package_network(50, 500, 500)
    d.create_circuit_network(123, 0.02)
    AccessNetworksList(d, root)
    root.mainloop()