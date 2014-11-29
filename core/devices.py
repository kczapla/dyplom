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


class CoreRouter(Router):
    def __init__(self, index, buffer_voice, buffer_video, buffer_be):
        super().__init__(index, buffer_voice, buffer_video, buffer_be)

        self.name = "CR " + str(index)


class Link:
    def __init__(self, name, length, capacity):

        self.index = name
        self.name = "Link " + str(name)
        self.length = length
        self.paths = {}
        self.capacity = capacity