__author__ = 'perun'
import core.networks as nw

interest_matrix = [[0.0, 0.2, 0.2, 0.2, 0.2, 0.2],
                   [0.2, 0.0, 0.2, 0.2, 0.2, 0.2],
                   [0.2, 0.2, 0.0, 0.2, 0.2, 0.2],
                   [0.2, 0.2, 0.2, 0.0, 0.2, 0.2],
                   [0.2, 0.2, 0.2, 0.2, 0.0, 0.2],
                   [0.2, 0.2, 0.2, 0.2, 0.2, 0.0]]

values = [{'intensity': 240, 'loss': 0.002, 'mode': 'c', 'index': 0},
          {'intensity': 350, 'loss': 0.002, 'mode': 'c', 'index': 1},
          {'intensity': 180, 'loss': 0.002, 'mode': 'c', 'index': 2},
          {'intensity': 12000, 'loss': 0, 'mode': 'p', 'index': 3},
          {'intensity': 16000, 'loss': 0, 'mode': 'p', 'index': 4},
          {'intensity': 15000, 'loss': 0, 'mode': 'p', 'index': 5}]

index = 5


def test_networks():

    for tmp in values:
        if tmp['mode'] == 'c':
            yield nw.Circuit(tmp['intensity'], tmp['index'], tmp['loss'])
        elif tmp['mode'] == 'p':
            yield nw.Package(tmp['intensity'], tmp['index'])