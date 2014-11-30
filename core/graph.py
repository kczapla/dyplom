__author__ = 'perun'

import networkx as nx
import core.devices as dev
import matplotlib.pyplot as plt

if __name__ == '__main__':

    G = nx.Graph()
    index = 0
    nodes = []
    links = []

    for x in range(6):
        nodes.append(dev.EdgeRouter(index, 5, 15, 30))
        index += 1

    for x in range(5):
        nodes.append(dev.CoreRouter(index, 5, 15, 30))
        index += 1

    G.add_nodes_from(nodes)
              #      EDGE      |     CORE
             #1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11
    matrix = [
             [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],  # 1
             [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],  # 2
             [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],  # 3
             [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0],  # 4
             [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],  # 5
             [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],  # 6
             [0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0],  # 7
             [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1],  # 8
             [0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0],  # 9
             [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0],  # 10
             [0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0]]  # 11

    #nx.draw(G)
    #plt.show()

    connections = [(matrix.index(x), i) for x in matrix for i, j in enumerate(x) if j == 1]

    for x in connections:
        links.append(dev.Link(x, 50, 300000000))

    for x in links:
        print(x.index)

    for x in links:
        a, b = x.index
        G.add_edge(nodes[a], nodes[b], weight=50)

    nx.draw(G)
    plt.show()

ll



    #G.add_node(1)
    #H = nx.path_graph(10)
    #G.add_nodes_from(H)
