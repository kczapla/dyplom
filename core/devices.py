__author__ = 'perun'

import core.calculations as calc


class Router:
    def __init__(self, index, buffer_voice, buffer_video, buffer_be):

        self.index = index

        self.buffer_voice = buffer_voice
        self.buffer_video = buffer_video
        self.buffer_be = buffer_be

        self.loss = 0


class EdgeRouter(Router):
    def __init__(self, index, buffer_voice, buffer_video, buffer_be):
        super().__init__(index, buffer_voice, buffer_video, buffer_be)

        self.name = "ER " + str(index)

        self.flow_voice_in = 0
        self.flow_video_in = 0
        self.flow_be_in = 0

        self.flow_voice = 0
        self.flow_video = 0
        self.flow_be = 0

        self.connected = False
        self.connected_index = ''

    def set_name(self, index):

        """
        Method is setting the new name based of index of the router
        :param index: new value of router index
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
        self.flow_voice_in = 0
        self.flow_video_in = 0
        self.flow_be_in = 0

        self.flow_voice = 0
        self.flow_video = 0
        self.flow_be = 0

        self.connected = False
        self.connected_index = ''


class CoreRouter(Router):
    def __init__(self, index, buffer_voice, buffer_video, buffer_be):
        super().__init__(index, buffer_voice, buffer_video, buffer_be)

        self.name = "CR " + str(index)

    def set_name(self, index):

        """
        Method is setting the new name based of index of the router
        :param index: new value of router index
        """
        self.index = index
        self.name = "CR " + str(index)


class Link:
    def __init__(self, index, length, capacity):

        self.index = index
        self.name = "Link " + str(index)
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
        self.iplr_void = 0
        self.iplr_be = 0

        self.ipdt_voice = 0
        self.ipdt_video = 0
        self.ipdt_be = 0

    def calculate_ipdt(self, nodes, package_voice, package_video, package_be):

        for x in nodes:
            if self.index[1] == x.index:
                calc.ipdt(self, x, package_voice, package_video, package_be)

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

        self.flow_voice_up = 0
        self.flow_video_up = 0
        self.flow_be_up = 0

        self.flow_voice_down = 0
        self.flow_video_down = 0
        self.flow_be_down = 0

        self.flow_voice = 0
        self.flow_video = 0
        self.flow_be = 0
