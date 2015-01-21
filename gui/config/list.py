__author__ = 'perun'


def access_network_list_circuit(instance):
    rows = [('Network name: ', instance.__dict__['name']),
            ('Type of network', type(instance).__name__),
            ('Index of network', instance.__dict__['index']),
            ('Voice intensity in [Erl]', instance.__dict__['intensity_voice_in']),
            ('Voice intensity out [Erl]', instance.__dict__['intensity_voice_out']),
            ('Links in', instance.__dict__['links_in']),
            ('Links out', instance.__dict__['links_out']),
            ('Number of DSP in', instance.__dict__['dsp_in']),
            ('Number of DSP out', instance.__dict__['dsp_out']),
            ('Voice flow in [b/s]', instance.__dict__['flow_voice_in']),
            ('Voice flow out [b/s]', instance.__dict__['flow_voice_out']),
            ('Probability of loss', instance.__dict__['loss']),
            ('Voice codec', instance.__dict__['chosen_voice_codec']),
            ('Voice package length', instance.__dict__['package_voice_length'])]
    return rows


def access_network_list_package(instance):
        rows = [('Network name: ', instance.__dict__['name']),
                ('Type of network', type(instance).__name__),
                ('Index of network', instance.__dict__['index']),
                ('Voice intensity in [1/s]', instance.__dict__['intensity_voice_in']),
                ('Voice intensity out [1/s]', instance.__dict__['intensity_voice_out']),
                ('Video intensity in [1/s]', instance.__dict__['intensity_video_in']),
                ('Video intensity out [1/s]', instance.__dict__['intensity_video_out']),
                ('BE intensity in [1/s]', instance.__dict__['intensity_be_in']),
                ('BE intensity out [1/s]', instance.__dict__['intensity_be_out']),
                ('Voice flow in [b/s]', instance.__dict__['flow_voice_in']),
                ('Voice flow out [b/s]', instance.__dict__['flow_voice_out']),
                ('Video flow in [b/s]', instance.__dict__['flow_video_in']),
                ('Video flow out [b/s]', instance.__dict__['flow_video_out']),
                ('BE flow in [b/s]', instance.__dict__['flow_be_in']),
                ('BE flow out [b/s]', instance.__dict__['flow_be_out']),
                ('Voice codec', instance.__dict__['chosen_voice_codec']),
                ('Voice package length [bit]', instance.__dict__['package_voice_length']),
                ('Video codec', instance.__dict__['chosen_video_codec']),
                ('Video package length [bit]', instance.__dict__['package_length_h264']),
                ('BE codec', instance.__dict__['chosen_be_protocol']),
                ('BE package length [bit]', instance.__dict__['package_length_be'])]

        return rows


def nodes_list_edge(instance):
    rows = [('Node name: ', instance.__dict__['name']),
            ('Type of node', type(instance).__name__),
            ('Index of node', instance.__dict__['index']),
            ('Size of voice buffer', instance.__dict__['buffer_voice']),
            ('Size of video buffer', instance.__dict__['buffer_video']),
            ('Size of be buffer', instance.__dict__['buffer_be']),
            ('Voice flow through the router [b/s]', instance.__dict__['flow_voice']),
            ('Video flow through the router [b/s]', instance.__dict__['flow_video']),
            ('Be flow through the router [b/s]', instance.__dict__['flow_be'])]
    return rows


def nodes_list_core(instance):
    rows = [('Node name: ', instance.__dict__['name']),
            ('Type of node', type(instance).__name__),
            ('Index of node', instance.__dict__['index']),
            ('Size of voice buffer', instance.__dict__['buffer_voice']),
            ('Size of video buffer', instance.__dict__['buffer_video']),
            ('Size of be buffer', instance.__dict__['buffer_be'])]
    return rows


def links_list(instance):
    rows = [('Link name', instance.__dict__['name']),
            ('Type of link', type(instance).__name__),
            ('Index of node', instance.__dict__['index']),
            ('Length [km]', instance.__dict__['length']),
            ('Capacity [b/s]', instance.__dict__['capacity']),
            ('Flow voice up [b/s]', instance.__dict__['flow_voice_up']),
            ('Flow video up [b/s]', instance.__dict__['flow_video_up']),
            ('Flow be up [b/s]', instance.__dict__['flow_be_up']),
            ('Flow voice down [b/s]', instance.__dict__['flow_voice_down']),
            ('Flow video down [b/s]', instance.__dict__['flow_video_down']),
            ('Flow be down [b/s]', instance.__dict__['flow_be_down']),
            ('Flow voice both [b/s]', instance.__dict__['flow_voice']),
            ('Flow video both [b/s]', instance.__dict__['flow_video']),
            ('Flow be both [b/s]', instance.__dict__['flow_be']),
            ('IPLR for voice', instance.__dict__['iplr_voice']),
            ('IPLR for video', instance.__dict__['iplr_video']),
            ('IPLR for be', instance.__dict__['iplr_be']),
            ('IPDT for voice [s]', instance.__dict__['ipdt_voice']),
            ('IPDT for video [s]', instance.__dict__['ipdt_video']),
            ('IPDT for be [s]', instance.__dict__['ipdt_be']),
            ('IPDV for voice [s]', instance.__dict__['ipdv_voice']),
            ('IPDV for video [s]', instance.__dict__['ipdv_video']),
            ('IPDV for be [s]', instance.__dict__['ipdv_be'])]
    return rows