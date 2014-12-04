__author__ = 'perun'


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

        self.flow_voice = 0
        self.flow_video = 0
        self.flow_be = 0

        self.connected = False
        self.connected_index = ''

    def set_name(self, index):

        self.index = index
        self.name = "ER " + str(index)

    def set_connected(self, status, index):
        self.connected = status
        self.connected_index = index


class CoreRouter(Router):
    def __init__(self, index, buffer_voice, buffer_video, buffer_be):
        super().__init__(index, buffer_voice, buffer_video, buffer_be)

        self.name = "CR " + str(index)

    def set_name(self, index):

        self.index = index
        self.name = "CR " + str(index)


class Link:
    def __init__(self, index, length, capacity):

        self.index = index
        self.name = "Link " + str(index)
        self.length = length
        self.paths = {}
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

    def set_flow_voice(self):
        self.flow_voice = self.flow_voice_down + self.flow_voice_up

    def set_flow_video(self):
        self.flow_video = self.flow_video_down + self.flow_video_up

    def set_flow_be(self):
        self.flow_be = self.flow_be_down + self.flow_be_up