__author__ = 'perun'

import core.calculations as calc


class Router:
    def __init__(self, name, index, buffer_voice, buffer_video, buffer_be):

        self.index = index

        self.buffer_voice = buffer_voice
        self.buffer_video = buffer_video
        self.buffer_be = buffer_be

        self.name = name

        self.loss = 0

    def reset_resources(self):
        pass

    def edit(self, name, buffer_voice, buffer_video, buffer_be):
        """
        Method edits values of router
        :param name: new name. If empty name will be unchanged
        :param buffer_voice: size of voice buffer
        :param buffer_video: size of video buffer
        :param buffer_be: size of be buffer
        """
        if name:
            self.name = name
        self.buffer_voice = buffer_voice
        self.buffer_video = buffer_video
        self.buffer_be = buffer_be


class EdgeRouter(Router):
    def __init__(self, name, index, buffer_voice, buffer_video, buffer_be):
        Router.__init__(self, name, index, buffer_voice, buffer_video, buffer_be)

        self.flow_voice_in = 0
        self.flow_video_in = 0
        self.flow_be_in = 0

        self.flow_voice = 0
        self.flow_video = 0
        self.flow_be = 0

        self.connected = False
        self.connected_index = None

    def set_name(self, index):

        """
        Method is setting the new name based of index_networks of the router
        :param index: new value of router index_networks
        """
        self.index = index
        self.name = "ER " + str(index)

    def set_connected(self, status, index):

        """
        Method is responsible for handling connection between network and router
        :param status: status of connected variable. Can be true of false
        :param index: Index of network
        """
        self.connected = status
        self.connected_index = index

    def reset_resources(self):

        """
        Method is responsible for resenting resources of current object

        """

        self.connected = False
        self.connected_index = ''


class CoreRouter(Router):
    def __init__(self, name, index, buffer_voice, buffer_video, buffer_be):
        Router.__init__(self, name, index, buffer_voice, buffer_video, buffer_be)

    def set_name(self, index):

        """
        Method is setting the new name based of index_networks of the router
        :param index: new value of router index_networks
        """
        self.index = index
        self.name = "CR " + str(index)


class Link:
    def __init__(self, name, index, length, capacity):

        self.index = index
        self.name = name
        self.length = length
        self.paths_voice = {}
        self.paths_video = {}
        self.paths_be = {}
        self.capacity = capacity

        self.flow_voice_up = 0
        self.flow_video_up = 0
        self.flow_be_up = 0

        self.flow_voice_down = 0
        self.flow_video_down = 0
        self.flow_be_down = 0

        self.flow_voice = 0
        self.flow_video = 0
        self.flow_be = 0

        self.iplr_voice = 0
        self.iplr_video = 0
        self.iplr_be = 0

        self.ipdt_voice = 0
        self.ipdt_video = 0
        self.ipdt_be = 0

        self.ipdv_voice = 0
        self.ipdv_video = 0
        self.ipdv_be = 0

        self.a_voice = 0
        self.a_video = 0

        self.ipdv_max_voice = 0
        self.ipdv_max_video = 0
        self.ipdv_max_be = 0

        self.ipdv_min_voice = 0
        self.ipdv_min_video = 0
        self.ipdv_min_be = 0

    def calculate_ipdv(self, nodes, package_voice, package_video, package_be):

        for x in nodes:
            if self.index[1] == x.index:
                calc.ipdv(self, x, package_voice, package_video, package_be)
                break

    def calculate_ipdt(self, nodes, package_voice, package_video, package_be):

        for x in nodes:
            if self.index[1] == x.index:
                calc.ipdt(self, x, package_voice, package_video, package_be)
                break

    def calculate_iplr(self, nodes):

        for x in nodes:
            if self.index[1] == x.index:
                calc.iplr(self, x)
                break

    def set_flow_voice(self):

        """
        Sums up both ways traffic for voice stream

        """
        self.flow_voice = self.flow_voice_down + self.flow_voice_up

    def set_flow_video(self):

        """
        Sums up both ways traffic for video stream

        """
        self.flow_video = self.flow_video_down + self.flow_video_up

    def set_flow_be(self):

        """
        Sums up both ways traffic for be stream

        """
        self.flow_be = self.flow_be_down + self.flow_be_up

    def reset_resources(self):

        """
        Method is responsible for resenting resources of current object

        """

        self.paths_voice = {}
        self.paths_video = {}
        self.paths_be = {}

        self.flow_voice_up = 0
        self.flow_video_up = 0
        self.flow_be_up = 0

        self.flow_voice_down = 0
        self.flow_video_down = 0
        self.flow_be_down = 0

        self.flow_voice = 0
        self.flow_video = 0
        self.flow_be = 0

        self.iplr_voice = 0
        self.iplr_video = 0
        self.iplr_be = 0

        self.ipdt_voice = 0
        self.ipdt_video = 0
        self.ipdt_be = 0

        self.ipdv_voice = 0
        self.ipdv_video = 0
        self.ipdv_be = 0

    def edit(self, name, length, capacity):
        print('class: {}, method: edit()'.format(type(self).__name__))
        if name:
            self.name = name
        else:
            self.name = self.name
        self.length = length
        self.capacity = capacity