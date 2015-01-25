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
    a = float(link.flow_be / (link.capacity - link.flow_voice - link.flow_video))
    link.iplr_be = float(((1 - a) / (1 - pow(a, node.buffer_be + 2))) * pow(a, node.buffer_be + 1))


def ipdt(link, node, package_voice, package_video, package_be):

    # speed of light in optical fibre 200,000 km/s
    c = 200000

    a = float(link.flow_voice / link.capacity)
    mi = float(link.capacity / package_voice)
    num = float(1 + pow(a, node.buffer_voice) * (node.buffer_voice * a - (node.buffer_voice + 1)))
    dnom = float((1 - a) * (1 - pow(a, node.buffer_voice + 2)))
    t_ocz = float((a/mi)*(num/dnom))
    t_nad = float(1/mi)
    t_prop = float(link.length/c)
    link.ipdt_voice = t_nad + t_ocz + t_prop

    if link.flow_video > 0:
        a = float(link.flow_video / (link.capacity - link.flow_voice))
        mi = float(link.capacity / package_video)
        num = float(1 + pow(a, node.buffer_video) * (node.buffer_video * a - (node.buffer_video + 1)))
        dnom = float((1 - a) * (1 - pow(a, node.buffer_video + 2)))
        t_ocz = float((a/mi)*(num/dnom))
        t_prop = float(link.length/c)
        t_nad = float(1/mi)
        link.ipdt_video = t_nad + t_ocz + t_prop
    else:
        link.ipdt_video = 0

    if link.flow_be > 0:
        a = float(link.flow_be / (link.capacity - link.flow_voice - link.flow_video))
        mi = float(link.capacity / package_be)
        num = float(1 + pow(a, node.buffer_be) * (node.buffer_be * a - (node.buffer_be + 1)))
        dnom = float((1 - a) * (1 - pow(a, node.buffer_be + 2)))
        t_ocz = float((a/mi)*(num/dnom))
        t_prop = float(link.length/c)
        t_nad = float(1/mi)
        link.ipdt_be = t_nad + t_ocz + t_prop
    else:
        link.ipdt_be = 0


def ipdv(link, node, package_voice, package_video, package_be):

    t_nad_voice = float(package_voice / link.capacity)
    t_nad_video = float(package_video / link.capacity)
    t_nad_be = float(package_be / link.capacity)

    ipdt_max_voice = (node.buffer_voice - 1) * t_nad_voice + t_nad_be
    ipdt_min_voice = t_nad_voice
    link.ipdv_voice = ipdt_max_voice - ipdt_min_voice

    a_voice = float(link.flow_voice / link.capacity)
    link.a_voice = a_voice
    a_video = float(link.flow_video/(link.capacity - link.flow_voice))
    link.a_video = a_video

    if link.flow_video > 0:
        num = float((node.buffer_video - 1) * t_nad_video + t_nad_be)
        dnom = float(1 - a_voice)
        ipdt_max_video = float(num/dnom)
        link.ipdv_max_video = ipdt_max_video
        ipdt_min_video = t_nad_video
        link.ipdv_min_video = t_nad_video
        link.ipdv_video = float(ipdt_max_video - ipdt_min_video)
    else:
        link.ipdv_video = 0

    if link.flow_be > 0:
        num = float((node.buffer_be - 1) * t_nad_be)
        dnom = float(1 - a_voice - a_video)
        ipdt_max_be = float(num/dnom)
        link.ipdv_max_be = ipdt_max_be
        ipdt_min_be = t_nad_be
        link.ipdv_min_be = t_nad_be
        link.ipdv_be = float(ipdt_max_be - ipdt_min_be)
    else:
        link.ipdv_be = 0


def expected_value(value, probability):
    """
    Method calculates expected value
    :param value: value of discreet variable
    :param probability: probability of 
    :return:
    """
    return value * probability


def test():
    print(expected_value(400, 0.4)+expected_value(960, 0.6))


if __name__ == '__main__':
    test()
