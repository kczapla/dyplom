__author__ = 'perun'

import core.distribution as dist
import core.menu as menu


if __name__ == '__main__':

    d = dist.Data()

    while True:
        print("""++++++++++++++++++++++++OPTIONS++++++++++++++++++++++++
                (1) - CREATE ACCESS NETWORKS
                    (1.1) - CIRCUIT
                    (1.2) - PACKAGE
                (2) - DELETE NETWORK
                (3) - CREATE INTEREST MATRIX
                    (3.1) - VOICE
                    (3.2) - VIDEO
                    (3.3) - BEST EFFORT
                (4) - CHANGE INTEREST MATRIX
                    (4.1) - VOICE
                    (4.2) - VIDEO
                    (4.3) - BEST EFFORT
                (5) - CREATE NODES IN CORE NETWORK
                    (5.1) - EDGE ROUTER
                    (5.2) - CORE ROUTER
                (6) - DELETE NODE
                (7) - CREATE ADJACENCY MATRIX
                (8) - CHANGE ADJACENCY MATRIX
                (9) - CREATE LINKS BETWEEN NODES
                (10) - CONNECT NETWORKS WITH CORE
                (11) - SET PATHS BETWEEN NODES
                    (11.1) - VOICE TRAFFIC
                    (11.2) - VIDEO TRAFFIC
                    (11.3) - BE TRAFFIC
                (12) - PROCESS DATA
                    (12.1) - RESOURCES ON THE EDGE OF ACCESS NETWORK
                (13) - SHOW DATA
                (14) - USE TEST VALUES
                (15) - SHOW INTEREST MATRIX
                (16) - EXIT PROGRAM
                ++++++++++++++++++++++++OPTIONS++++++++++++++++++++++++""")
        option = str(input('Your choice: '))

        if '1.' in option:

                if option == '1.1':
                    intensity_voice = int(input('Intensity of voice stream: '))
                    loss = float(input('Loss probability: '))

                    if intensity_voice and loss:
                        d.create_circuit_network(intensity_voice, loss)
                    else:
                        print('Wrong values. Try again.')

                elif option == '1.2':
                    intensity_voice = int(input('Intensity of voice stream: '))
                    intensity_video = int(input('Intensity of video stream: '))
                    intensity_be = int(input('Intensity of be stream: '))

                    if not intensity_voice:
                        intensity_voice = 0
                    if not intensity_video:
                        intensity_video = 0
                    if not intensity_be:
                        intensity_be = 0

                    d.create_package_network(intensity_voice, intensity_video, intensity_be)
                else:
                    print('Wrong value! Try again.')

        elif '2.' in option:
            if d.networks:
                print('Select netowrk to delete from list below:')
                menu.print_nodes(d.networks)
                index = int(input('Index of network: '))
                if type(index) is int and 0 <= index < d.index_networks:
                    d.delete_network(index)
                else:
                    print('Network doesn\'t exist. Try again.')
            else:
                print('Before operation create networks! Try again.')

        elif '3.' in option:
            if d.networks:
                if option == '3.1':
                    print('INTEREST MATRIX VOICE')
                    print('Size of matrix: {}'.format(d.index_networks))
                    print('Insert data as on example. \n Example: \n Row[N]: value1, value2, ..., valueN')
                    tmp = menu.interest_matrix(d.index_networks)
                    if not tmp:
                        print('To much values in single row. Try again.')
                    else:
                        d.set_interest_matrix_voice(tmp)
                elif option == '3.2':
                    print('INTEREST MATRIX VIDEO')
                    print('Size of matrix: {}'.format(d.index_networks))
                    print('Insert data as on example. \n Example: \n Row[N]: value1, value2, ..., valueN')
                    tmp = menu.interest_matrix(d.index_networks)
                    if not tmp:
                        print('To much values in single row. Try again.')
                    else:
                        d.set_interest_matrix_video(tmp)
                elif option == '3.3':
                    print('INTEREST MATRIX BE')
                    print('Size of matrix: {}'.format(d.index_networks))
                    print('Insert data as on example. \n Example: \n Row[N]: value1, value2, ..., valueN')
                    tmp = menu.interest_matrix(d.index_networks)
                    if not tmp:
                        print('To much values in single row. Try again.')
                    else:
                        d.set_interest_matrix_be(tmp)
                else:
                    print('Wrong value! Choose from available options.')

        elif option == '4':
            if option == '4.1':
                if d.interest_matrix_voice:
                    index = int(input('Set row to change: '))
                    if type(index) is int and 0 <= index < d.index_networks:
                        row = menu.single_row_interest(index)
                        if not row:
                            print('To many values in single row. Try again.')
                        else:
                            d.change_single_value_interest_matrix_voice(index, row)
                    else:
                        print('Wrong value! Try again.')
            elif option == '4.2':
                if d.interest_matrix_video:
                    index = int(input('Set row to change: '))
                    if type(index) is int and 0 <= index < d.index_networks:
                        row = menu.single_row_interest(index)
                        if not row:
                            print('To many values in single row. Try again.')
                        else:
                            d.change_single_value_interest_matrix_video(index, row)
                    else:
                        print('Wrong value! Try again.')
            elif option == '4.3':
                if d.interest_matrix_be:
                    index = int(input('Set row to change: '))
                    if type(index) is int and 0 <= index < d.index_networks:
                        row = menu.single_row_interest(index)
                        if not row:
                            print('To many values in single row. Try again.')
                        else:
                            d.change_single_value_interest_matrix_be(index, row)
                    else:
                        print('Wrong value! Try again.')
            else:
                print('Option doesnt exists! Try again.')

        elif option == '5':
            if option == '5.1':
                buffer_voice = int(input('Size of voice buffer: '))
                buffer_video = int(input('Size of voice buffer: '))
                buffer_be = int(input('Size of voice buffer: '))
                if buffer_voice and buffer_video and buffer_be:
                    d.create_node_edge(buffer_voice, buffer_video, buffer_be)
                else:
                    print('Set all values! Try again.')
            elif option == '5.2':
                buffer_voice = int(input('Size of voice buffer: '))
                buffer_video = int(input('Size of voice buffer: '))
                buffer_be = int(input('Size of voice buffer: '))
                if buffer_voice and buffer_video and buffer_be:
                    d.create_node_core(buffer_voice, buffer_video, buffer_be)
                else:
                    print('Set all values! Try again.')
            else:
                print('Before operation create networks! Try again.')

        elif option == '6':
            print('Select node to delete from list below:')
            menu.print_nodes(d.nodes)
            index = int(input('Index of node: '))
            if type(index) and 0 <= index < d.index_nodes:
                d.delete_node(index)
            else:
                print('Wrong value or node doesnt exsit! Try again')

        elif option == '7':
            if d.nodes:
                print('ADJACENCY MATRIX')
                print('Size of matrix: {}'.format(d.index_nodes))
                print('Insert data as on example. \n Example: \n Row[N]: value1, value2, ..., valueN')
                tmp = menu.adjacency_matrix(d.index_nodes)
                if not tmp:
                    print('To much values in single row. Try again.')
                else:
                    d.create_adjacency_matrix(tmp)
            else:
                print('Wrong value! Choose from available options.')

        elif option == '8':

            if d.adjacency_matrix:
                    menu.print_matrix(d.adjacency_matrix)
                    row = int(input('Select row to change: '))
                    if type(row) is int and 0 <= row < d.index_networks:
                        tmp = menu.single_row_adjacency(row)
                        if not row:
                            print('To many values in single row. Try again.')
                        else:
                            d.change_single_value_interest_matrix_voice(row, menu.single_row_adjacency(row))
                    else:
                        print('Wrong value! Try again.')

        elif option == '9':
            pass

        elif option == '10':
            if d.networks and d.nodes:
                print('CONNECTING ACCESS NETWORK WITH EDGE ROUTER')
                print('Networks to connect: ')
                menu.print_nodes(d.networks)
                print('Edge routers to connect: ')
                menu.print_edge_nodes(d.nodes)
                d.create_net_edge_matrix(menu.access_edge(d.networks))
            else:
                print('Networks or nodes doesnt exist. Create them before choosing this option.')

        elif option == '11':
            print('CREATE PATHS')
            print('Nodes to connect: ')
            menu.print_nodes(d.nodes)
            print('As a first and the last value insert the index of edge router')
            print('Insert data as on example. \n Example: \n Path[N]: ER N, node 1, ..., node i, ER M')
            if option == '11.1':
                d.create_paths_matrix_voice(menu.paths())
            elif option == '11.2':
                d.create_paths_matrix_video(menu.paths())
            elif option == '11.3':
                d.create_paths_matrix_be(menu.paths())

        elif option == '12':
            pass