__author__ = 'perun'
import core.networks as nw
import core.devices as dev

interest_matrix = [[0.0, 0.2, 0.2, 0.2, 0.2, 0.2],
                   [0.2, 0.0, 0.2, 0.2, 0.2, 0.2],
                   [0.2, 0.2, 0.0, 0.2, 0.2, 0.2],
                   [0.2, 0.2, 0.2, 0.0, 0.2, 0.2],
                   [0.2, 0.2, 0.2, 0.2, 0.0, 0.2],
                   [0.2, 0.2, 0.2, 0.2, 0.2, 0.0]]

intrest_matrix_video = [[0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0.5, 0.5],
                        [0, 0, 0, 0.5, 0, 0.5],
                        [0, 0, 0, 0.5, 0.5, 0]]

interest_matrix_be = [[0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0.5, 0.5],
                     [0, 0, 0, 0.5, 0, 0.5],
                     [0, 0, 0, 0.5, 0.5, 0]]

values = [{'intensity': 240, 'mode': 'c', 'loss': 0.002,  'index': 0},
          {'intensity': 350, 'mode': 'c', 'loss': 0.002,  'index': 1},
          {'intensity': 180, 'mode': 'c', 'loss': 0.002,  'index': 2},
          {'index': 3, 'mode': 'p', 'intensity': 12000, 'intensity_video': 18000, 'intensity_be': 18000},
          {'index': 4, 'mode': 'p',  'intensity': 16000, 'intensity_video': 20000, 'intensity_be': 20000},
          {'index': 5, 'mode': 'p', 'intensity': 15000, 'intensity_video': 19000, 'intensity_be': 19000}]

index = 6


def test_networks():

    for tmp in values:
        if tmp['mode'] == 'c':
            yield nw.Circuit(tmp['index'], tmp['intensity'], tmp['loss'])
        elif tmp['mode'] == 'p':
            yield nw.Package(tmp['index'], tmp['intensity'], tmp['intensity_video'], tmp['intensity_be'])

             #      EDGE      |     CORE
         #1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11
matrix = [
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],  # 1
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],  # 2
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],  # 3
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],  # 4
         [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],  # 5
         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],  # 6
         [1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0],  # 7
         [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1],  # 8
         [0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0],  # 9
         [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0],  # 10
         [0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0]]  # 11

connections = [(matrix.index(x), i) for x in matrix for i, j in enumerate(x) if j == 1]

#print(connections)

index_routers = 11


def test_routers():
        for x in range(index_routers):
            if x < 6:
                yield dev.EdgeRouter(index, 5, 15, 30)
            else:
                yield dev.CoreRouter(index, 5, 15, 30)


def test_links():
    for x in connections:
        yield dev.Link(x, 50, 300000000)