__author__ = 'perun'


def erlang_first_formula(intensity=None, loss_ratio=None):
    """
    Erlang B-Formula
    :param intensity: Intensity of the stream of date to or from network
    :param loss_ratio: Probability of losing data
    :return: Method returns number of lines need to provide demanded loss ratio for given intensity
    """
    b = 1
    n = 1

    while b > loss_ratio:
        b = (intensity * b) / (intensity * b + n)
        n += 1

    return n - 1


def pcm_lines(n=None):
    """

    :param n: Number of lines
    :return: Number of pcm lines
    """
    return round(n / 30 + 0.49)


def real_links(pcm=None):
    """

    :param pcm: Number of pcm lines
    :return: The actual number of link lines
    """
    return pcm * 30


def dsp(nr=None, ldsp=4):
    """

    :param nr: The actual number of pcm lines
    :param ldsp: Number of lines per one digital signal processor
    :return: Number of signal processors on the edge of the network
    """
    return round(nr / ldsp + 0.49)


def out_intensity(network=None):
    """
        Method is counting the output intensity of the network.
        :param network:
        """
    for y in network:
        for x in network:
            y.intensity_out += x.intensity_in * x.interest_row[y.index]


def iplr(link, node):
    """
    Method is calculating value of IP loos ratio parameter
    :param link: object of link between nodes
    :param node: object of node from which size of buffer will be taken
    """
    # voice
    a = float(link.flow_voice / link.capacity)
    link.iplr_voice = float(((1 - a) / (1 - pow(a, node.buffer_voice + 2))) * pow(a, node.buffer_voice + 1))

    # video
    a = float(link.flow_video / (link.capacity - link.flow_voice))
    link.iplr_video = float(((1 - a) / (1 - pow(a, node.buffer_video + 2))) * pow(a, node.buffer_video + 1))

    #be
    a = float(link.flow_be / (link.capacity - (link.flow_voice + link.flow_video)))
    link.iplr_be = float(((1 - a) / (1 - pow(a, node.buffer_be + 2))) * pow(a, node.buffer_be + 1))


def ipdt(link, node, package_voice, package_video, package_be):

    a = float(link.flow_voice / link.capacity)
    mi = float(link.capacity / package_voice)
    num = float(1 + pow(a, node.buffer_voice) * (node.buffer_voice * a - (node.buffer_voice + 1)))
    dnom = float((1 - a) * (1 - pow(a, node.buffer_voice + 2)))
    link.ipdt_voice = float((a/mi)*(num/dnom))


    a = float(link.flow_video / (link.capacity - link.flow_voice))
    mi = float(link.capacity / package_video)
    num = float(1 + pow(a, node.buffer_video) * (node.buffer_video * a - (node.buffer_video + 1)))
    dnom = float((1 - a) * (1 - pow(a, node.buffer_video + 2)))
    link.ipdt_video = float((a/mi)*(num/dnom))

    a = float(link.flow_video / (link.capacity - link.flow_voice))
    mi = float(link.capacity / package_be)
    num = float(1 + pow(a, node.buffer_be) * (node.buffer_be * a - (node.buffer_be + 1)))
    dnom = float((1 - a) * (1 - pow(a, node.buffer_be + 2)))
    link.ipdt_be = float((a/mi)*(num/dnom))

   #a = float(link.flow_be / (link.capacity - (link.flow_voice + link.flow_video)))
    #link.ipdt_be = float(((a * package_be) / link.capacity) * ((1 + pow(a, node.buffer_be)
     #                                                           * (node.buffer_be * a - (node.buffer_be + 1)))
      #                                                         / (
       # (1 - node.buffer_be) * (1 - pow(a, node.buffer_be + 2)))))