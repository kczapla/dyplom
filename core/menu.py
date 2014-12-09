__author__ = 'perun'


def interest_matrix(length):
    tmp = [input('Row [{}]: '.format(x)) for x in range(length)]
    matrix = [[float(j) for j in i.split(',')] for i in tmp]
    for x in matrix:
        if len(x) >= length:
            return False
    return matrix


def single_row_interest(index):
    tmp = input('Row [{}]: '.format(index))
    row = [float(x) for x in tmp.split(',')]
    if len(row) >= index:
        return False
    return row


def single_row_adjacency(index):
    tmp = input('Row [{}]: '.format(index))
    row = [int(x) for x in tmp.split(',')]
    if len(row) >= index:
        return False
    return row


def print_nodes(nodes):
    for x in nodes:
        print(x.name, end=', ')


def print_edge_nodes(nodes):
    for x in nodes:
        if 'ER' in x.name:
            print(x, end=', ')


def print_matrix(matrix):
    for x in matrix:
        print(x)


def adjacency_matrix(length):
    tmp = [input('Row [{}]: '.format(x)) for x in range(length)]
    matrix = [[int(j) for j in i.split(',')] for i in tmp]
    for x in matrix:
        if len(x) >= length:
            return False
    return matrix


def access_edge(networks):
    tmp = [[x.index, int(input('Connect network {} with edge router: '.format(x.name)))] for x in networks]
    return tmp


def paths():
    number = int(input('Number of paths: '))
    tmp = [input('Path {}: '.format(x)) for x in range(number)]
    matrix = [[int(j) for j in i.split(',')] for i in tmp]
    return matrix


def links(connections):
    x = 1000000
    return [[index, int(input('Length of link {} (in km): '.format(index))),
             int(input('Capacity of link (in Mb/s)')) * x] for index in connections]
