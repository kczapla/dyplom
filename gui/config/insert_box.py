__author__ = 'perun'


def access_network_circuit_insertbox():
    circuit_entry_fields = 'Name', 'Voice latency [Erl]', 'Loss probability'
    return circuit_entry_fields


def access_network_package_insertbox():
    package_entry_fields = ('Name', 'Voice latency [Pack/s]', 'Video latency [Pack/s]', 'BE latency [Pack/s]',
                            'Video package length [B]', 'Be package length [B]')
    return package_entry_fields


def node_insertbox():
    edge_entry_fields = 'Name', 'Size of voice buffer', 'Size of video buffer', 'Size of be buffer'
    return edge_entry_fields


def link_inserbox():
    link_entry_fields = 'Name', 'Length [km]', 'Capacity [b/s]'
    return link_entry_fields