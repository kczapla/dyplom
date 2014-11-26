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
    return round(n/30+0.49)


def real_links(pcm=None):
    """

    :param pcm: Number of pcm lines
    :return: The actual number of link lines
    """
    return pcm*30


def dsp(nr=None, ldsp=4):
    """

    :param nr: The actual number of pcm lines
    :param ldsp: Number of lines per one digital signal processor
    :return: Number of signal processors on the edge of the network
    """
    return round(nr/ldsp+0.49)


def out_intensity(network=None):

        """
        Method is counting the output intensity of the network.
        :param network:
        """
        for y in network:
            for x in network:
                    y.intensity_out += x.intensity_in*x.interest_row[y.index]