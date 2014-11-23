__author__ = 'perun'

import core.calculations as calc


class Circuit:
    def __init__(self, intensity=None, index=None, loss=0.002):

        """


        :param intensity: Intensity which network generate to the core
        :param index: Index of the network
        :param loss: The probability of losing call. Need for the calculation of the network resources
        """
        #Values into the gateway from the network
        self.intensity_in = intensity
        self.links_in = 0
        self.pcm_in = 0
        self.r_in = 0
        self.dsp_in = 0
        self.flow_in = 0

        #Values out of the gateway to the network
        self.intensity_out = 0
        self.links_out = 0
        self.pcm_out = 0
        self.r_out = 0
        self.dsp_out = 0
        self.flow_out = 0

        #General values
        self.interest_row = []
        self.index = index
        self.name = "PSTN/ISDN/GSM " + str(index)
        self.loss = loss

    def input_resources(self):
        """
        Method is calculating input (to the core network) resources on the edge of the network. It's using methods from
        calculation module.
        """
        self.links_in = calc.erlang_first_formula(self.intensity_in, self.loss)
        self.pcm_in = calc.pcm_lines(self.links_in)
        self.r_in = calc.real_links(self.pcm_in)
        self.dsp_in = calc.dsp(self.r_in)

    def output_resources(self):
        """
        Method is calculating output (from the core network) resources on the edge of the network. It's using methods
        from calculation module.
        """
        self.links_out = calc.erlang_first_formula(self.intensity_out, self.loss)
        self.pcm_out = calc.pcm_lines(self.links_out)
        self.r_out = calc.real_links(self.pcm_out)
        self.dsp_out = calc.dsp(self.r_out)

    def reset_resources(self):
        #Values into the gateway from the network
        #self.intensity_in = 0
        #self.links_in = 0
        #self.pcm_in = 0
        #self.r_in = 0
        #self.dsp_in = 0
        #self.flow_in = 0

        #Values out of the gateway to the network
        self.intensity_out = 0
        self.links_out = 0
        self.pcm_out = 0
        self.r_out = 0
        self.dsp_out = 0
        self.flow_out = 0

    def out_intensity(self, networks=None):
        """
        Method is counting the output intensity of the network.
        :param networks: list of all created networks in the core
        """
        for x in networks:
            self.intensity_out += x.intensity_in*x.interest_row[self.index]

    def set_index(self, index):
        self.index = index
        self.set_name()

    def set_name(self):
        self.name = "PSTN/ISDN/GSM " + str(self.index)


class Package:
    def __init__(self, intensity_voice=0, index=None, intensity_video=0, intensity_mail=0):

        """

        :param intensity_voice: Intensity which network generate to the core
        :param index: Index of the network
        """
        #Values into the core network from access network
        self.intensity_voice_in = intensity_voice
        self.intensity_video_in = intensity_video
        self.intensity_mail_in = intensity_mail

        #this value is used to process with Circuit networks
        self.intensity_in = self.intensity_voice_in/100
        self.flow_in = 0

        #Values from the core network to the access network
        self.intensity_out = 0
        self.flow_out = 0

        #General values
        self.index = index
        self.name = "Dostęp IP " + str(index)
        self.loss = 0

    def reset_resources(self):
        #Values into the core network from access network
        #self.package_intensity_voice_in = 0
        #self.package_intensity_video_in = 0
        #self.package_intensity_mail_in = 0

        #self.intensity_in = 0
        #self.flow_in = 0

        #Values from the core network to the access network
        self.intensity_out = 0
        self.flow_out = 0

    def set_intensity_voice(self, n):
        self.intensity_voice_in = n
        self.intensity_in = self.intensity_voice_in/100

    def set_index(self, index):
        self.index = index
        self.set_name()

    def set_name(self):
        self.name = "Dostęp IP " + str(self.index)

    def out_intensity(self):
        pass