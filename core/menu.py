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