__author__ = 'perun'


def access_network_list_circuit(instance):
    rows = [('Network name: ', instance.__dict__['name']),
            ('Voice intensity in [Erl]', instance.__dict__['intensity_voice_in']),
            ('Voice intensity out [Erl]', instance.__dict__['intensity_voice_out']),
            ('Links in', instance.__dict__['links_in']),
            ('Links out', instance.__dict__['links_out']),
            ('Number of DSP in', instance.__dict__['dsp_in']),
            ('Number of DSP out', instance.__dict__['dsp_out']),
            ('Voice flow in [kb/s]', instance.__dict__['flow_voice_in']),
            ('Voice flow out [kb/s]', instance.__dict__['flow_voice_out']),
            ('Probability of loss', instance.__dict__['loss'])]
    return rows


def access_network_list_package(instance):
        rows = [('Network name: ', instance.__dict__['name']),
                ('Voice intensity in [1/s]', instance.__dict__['intensity_voice_in']),
                ('Voice intensity out [1/s]', instance.__dict__['intensity_voice_out']),
                ('Video intensity in [1/s]', instance.__dict__['intensity_video_in']),
                ('Video intensity out [1/s]', instance.__dict__['intensity_video_out']),
                ('BE intensity in [1/s]', instance.__dict__['intensity_be_in']),
                ('BE intensity out [1/s]', instance.__dict__['intensity_be_out']),
                ('Voice flow in [kb/s]', instance.__dict__['flow_voice_in']),
                ('Voice flow out [kb/s]', instance.__dict__['flow_voice_out']),
                ('Video flow in [kb/s]', instance.__dict__['flow_video_in']),
                ('Video flow out [kb/s]', instance.__dict__['flow_video_out']),
                ('BE flow in [kb/s]', instance.__dict__['flow_be_in']),
                ('BE flow out [kb/s]', instance.__dict__['flow_be_out'])]
        return rows