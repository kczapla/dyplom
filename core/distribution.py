__author__ = 'perun'

# import networkx as nx
import core.networks as nw
import core.test as test
import core.devices as dev


class Data:
    def __init__(self):

        """
        Method initialize interests matrix for 3 class of flow, list of creted by user networks and index_networks to handle
        operations on networks.

        """
        self.interest_matrix_voice = []
        self.interest_matrix_video = []
        self.interest_matrix_be = []
        self.networks = []
        self.index_networks = 0

        self.index_nodes = 0
        self.index_links = 0
        self.nodes = []
        self.links = []

        self.adjacency_matrix = []
        self.connections = []

        self.paths_matrix_voice = []
        self.paths_voice = []

        self.paths_matrix_video = []
        self.paths_video = []

        self.paths_matrix_be = []
        self.paths_be = []

        # variable have list with networks connected to core network
        self.net_edge = []

        self.iplr_for_paths_voice = {}
        self.iplr_for_paths_video = {}
        self.iplr_for_paths_be = {}

        self.ipdt_for_paths_voice = {}
        self.ipdt_for_paths_video = {}
        self.ipdt_for_paths_be = {}

        self.ipdv_for_paths_voice = {}
        self.ipdv_for_paths_video = {}
        self.ipdv_for_paths_be = {}

    # Methods connected with displaying Data class
    def process_data(self):

        for nets in self.networks:
            nets.reset_resources()

        for x in self.links:
            x.reset_resources()

        for x in self.nodes:
            if 'ER' in x.name:
                x.reset_resources()

        self.split_matrix()

        if self.interest_matrix_voice:
            for nets in self.networks:
                if 'GSM' in nets.name:
                    nets.set_intensity_voice_out(self.networks)

            for nets in self.networks:
                if 'GSM' in nets.name:
                    nets.input_resources()
                    nets.output_resources()

            for nets in self.networks:
                nets.set_flow_voice_in(self.networks)

            for nets in self.networks:
                nets.set_flow_voice_out(self.networks)

        for nets in self.networks:
            if not 'GSM' in nets.name:
                if self.interest_matrix_video:
                    nets.set_flow_video_in(self.networks)
                if self.interest_matrix_be:
                    nets.set_flow_be_in(self.networks)

        for nets in self.networks:
            if not 'GSM' in nets.name:
                if self.interest_matrix_video:
                    nets.set_flow_video_out(self.networks)
                if self.interest_matrix_be:
                    nets.set_flow_be_out(self.networks)

                    # for link in self.links:
                    #   link.calculate_iplr()

    def show_data(self):
        for x in self.networks:
            print("+++++++++++++++++")
            for y in (x.__dict__.keys()):
                print("{} = {}".format(y, x.__dict__[y]))
            print("+++++++++++++++++")

    def use_test_values(self):
        self.interest_matrix_voice = test.interest_matrix
        self.interest_matrix_video = test.intrest_matrix_video
        self.interest_matrix_be = test.interest_matrix_be
        for tmp in test.test_networks():
            self.networks.append(tmp)
            self.index_networks = test.index

            # Methods connected with processing Data class

    def create_circuit_network(self, intensity=0, loss=0):

        """
        Method is adding new circuit network, with values set by user, to the row of networks
        :param intensity: Intensity generated by network
        :param loss: loss probability
        """
        self.networks.append(nw.Circuit(self.index_networks, intensity, loss))
        self.index_networks += 1

    def create_package_network(self, intensity_voice=0, intensity_video=0, intensity_be=0):

        """
        Method is adding new package network, with values set by user, to the row of networks
        :param intensity_video: Video stream intensity generated by network
        :param intensity_be: BE stream intensity generated by network
        :param intensity_voice: Voice stream intensity generated by network
        """

        self.networks.append(nw.Package(self.index_networks, intensity_voice, intensity_video, intensity_be))
        self.index_networks += 1

    def delete_network(self, n=None):

        """
        Method is deleting selected network from the row of created networks. It also removes the row from an interest
        matrix belonging to deleted network. Finally it reorganise index_networks of existing networks and reprocess data.
        :param n: Index of network to delete
        """
        self.networks.pop(n)
        self.index_networks -= 1

        for x in range(self.index_networks):
            self.networks[x].set_index(x)

            if self.interest_matrix_voice:
                self.interest_matrix_voice[x].pop(n)
            if self.interest_matrix_video:
                self.interest_matrix_video[x].pop(n)
            if self.interest_matrix_be:
                self.interest_matrix_be[x].pop(n)

        if self.interest_matrix_voice:
            self.interest_matrix_voice.pop(n)

        if self.interest_matrix_video:
            self.interest_matrix_video.pop(n)

        if self.interest_matrix_be:
            self.interest_matrix_be.pop(n)

    def set_interest_matrix_voice(self, matrix):

        """
        Creating the interest matrix based on the number of networks
        """
        self.interest_matrix_voice = list()
        self.interest_matrix_voice = matrix
        # self.interest_matrix_voice = [[0, 1], [1, 0]]

    def set_interest_matrix_video(self, matrix):

        """
        Creating the interest matrix based on the number of networks
        """
        self.interest_matrix_video = list()
        self.interest_matrix_video = matrix
        # self.interest_matrix_video = [[0, 1], [1, 0]]

    def set_interest_matrix_be(self, matrix):

        """
        Creating the interest matrix based on the number of networks
        """
        self.interest_matrix_be = list()
        self.interest_matrix_be = matrix
        # self.interest_matrix_be = [[0, 1], [1, 0]]

    def split_matrix(self):

        """
        Method which partial interest matrix into row to every network
        :return: set the value of interest_row_voice in instance of the network class
        """
        for temp in self.networks:
            if self.interest_matrix_voice:
                temp.interest_row_voice = self.interest_matrix_voice[temp.index]

            if self.interest_matrix_video:
                temp.interest_row_video = self.interest_matrix_video[temp.index]

            if self.interest_matrix_be:
                temp.interest_row_be = self.interest_matrix_be[temp.index]

    def change_single_value_interest_matrix_voice(self, index, row):

        """

        :param row: row where variable is
        """
        self.interest_matrix_voice[index] = row

    def change_single_value_interest_matrix_video(self, index, row):
        self.interest_matrix_video[index] = row

    def change_single_value_interest_matrix_be(self, index, row):
        self.interest_matrix_be[index] = row

    # methods connected with graph operations
    def create_node_edge(self, buffer_voice, buffer_video, buffer_be):

        """

        :param buffer_voice: size of queue for voice traffic
        :param buffer_video: size of queue for video traffic
        :param buffer_be: size of queue for best effort traffic
        """
        self.nodes.append(dev.EdgeRouter(self.index_nodes, buffer_voice, buffer_video, buffer_be))
        self.index_nodes += 1

    def create_node_core(self, buffer_voice, buffer_video, buffer_be):

        """

        :param buffer_voice: size of queue for voice traffic
        :param buffer_video: size of queue for video traffic
        :param buffer_be: size of queue for best effort traffic
        """
        self.nodes.append(dev.CoreRouter(self.index_nodes, buffer_voice, buffer_video, buffer_be))
        self.index_nodes += 1

    def delete_node(self, index):

        self.nodes.pop(index)
        self.index_nodes -= 1

        # self.nodes = [self.nodes[x].set_name(x) for x in range(self.index_nodes)]
        for x in range(self.index_nodes):
            self.nodes[x].set_name(x)

        if self.adjacency_matrix:
            for x in self.adjacency_matrix:
                x.pop(index)

            self.adjacency_matrix.pop(index)
            self.slice_adjacency_matrix()
            self.create_links()

    def create_links(self):

        """
        Method is creating links between nodes
        """
        self.links = []
        # self.links = [dev.Link(x, int(input('Length: ')), int(input('Capacity: '))) for x in self.connections_sliced]
        self.links = [dev.Link(x, 50, 300000000) for x in self.connections]
        # self.links.append(dev.Link(index_networks, length, capacity))

    def create_adjacency_matrix(self, matrix):

        """
        Creating a splitting adjacency matrix.
        bug - self.adjacency_matrix.index_networks(x) returns '1' when matrix [[0, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0],
        [1, 0, 0, 0]] because this method is looking for first appearance of the value to appear. First is on the first
        row. Be aware of it!

        """
        self.adjacency_matrix = []
        # self.adjacency_matrix = ([[int(input('x[{}][{}] = '.format(lx, ly))) for ly in range(self.index_nodes)]
        # for lx in range(self.index_nodes)])
        # self.adjacency_matrix = [[0, 1, 0, 1, 1, 0], [1, 0, 1, 1, 0, 0], [0, 1, 0, 1, 1, 1], [1, 1, 1, 0, 0, 0],
        #                        [1, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0]]
        self.adjacency_matrix = matrix
        self.slice_adjacency_matrix()

    def slice_adjacency_matrix(self):

        self.connections = [[self.adjacency_matrix.index(x), i] for x in self.adjacency_matrix
                            for i, j in enumerate(x) if j == 1]

        for x in self.connections:
            for y in self.connections:
                tmp = y[:]
                tmp.reverse()
                if tmp == x:
                    self.connections.remove(y)

    def create_net_edge_matrix(self):

        self.net_edge = [[1, 0], [0, 5]]
        # self.net_edge = [[x.index_networks, int(input('Index of edge router to be connected with network {}: '.format(x.name)))]
        #                for x in self.networks]

    def create_paths_matrix_voice(self):

        self.paths_matrix_voice = []
        # self.paths_matrix_voice = ([[int(input('x[{}][{}] = '.format(lx, ly))) for ly in range(self.index_nodes)]
        # for lx in range(self.index_nodes)])
        self.paths_matrix_voice = [[5, 2, 1, 0], [0, 1, 3, 2, 5]]

        self.slice_paths_matrix_voice()

    def slice_paths_matrix_voice(self):

        self.paths_voice = [[] for x in self.paths_matrix_voice]

        for x in self.paths_matrix_voice:
            for y in range(len(x)):
                if y < len(x) - 1:
                    self.paths_voice[self.paths_matrix_voice.index(x)].append(x[y:y + 2])

    def create_paths_matrix_video(self):

        self.paths_matrix_video = []
        # self.paths_matrix_video = ([[int(input('x[{}][{}] = '.format(lx, ly))) for ly in range(self.index_nodes)]
        # for lx in range(self.index_nodes)])
        self.paths_matrix_video = [[5, 2, 1, 0], [0, 1, 3, 2, 5]]

        self.slice_paths_matrix_video()

    def slice_paths_matrix_video(self):

        self.paths_video = [[] for x in self.paths_matrix_video]

        for x in self.paths_matrix_video:
            for y in range(len(x)):
                if y < len(x) - 1:
                    self.paths_video[self.paths_matrix_video.index(x)].append(x[y:y + 2])

    def create_paths_matrix_be(self):

        self.paths_matrix_be = []
        # self.paths_matrix_be = ([[int(input('x[{}][{}] = '.format(lx, ly))) for ly in range(self.index_nodes)]
        # for lx in range(self.index_nodes)])
        self.paths_matrix_be = [[5, 2, 1, 0], [0, 1, 3, 2, 5]]

        self.slice_paths_matrix_be()

    def slice_paths_matrix_be(self):

        self.paths_be = [[] for x in self.paths_matrix_video]

        for x in self.paths_matrix_be:
            for y in range(len(x)):
                if y < len(x) - 1:
                    self.paths_be[self.paths_matrix_be.index(x)].append(x[y:y + 2])

    def set_connections(self):

        for x in self.net_edge:
            for y in self.networks:
                if x[0] == y.index:
                    for z in self.nodes:
                        if x[1] == z.index and 'ER' in z.name and not z.connected:
                            z.flow_voice = y.flow_voice_in
                            z.flow_video = y.flow_video_in
                            z.flow_be = y.flow_be_in
                            z.set_connected(True, y.name)
                            break

    def scatter_flow_voice(self):

        for x in self.paths_voice:
            for y in x:
                tmp = y[:]
                tmp.reverse()
                for z in self.links:
                    if y == z.index:
                        z.flow_voice_up += self.nodes[x[0][0]].flow_voice

                        # Writing the name of path going through link
                        z.paths_voice[str(x)] = self.nodes[x[0][0]].flow_voice

                        break

                    elif tmp == z.index:
                        z.flow_voice_down += self.nodes[x[0][0]].flow_voice

                        # Writing the name of path going through link
                        z.paths_voice[str(x)] = self.nodes[x[0][0]].flow_voice

                        break

    def scatter_flow_video(self):

        for x in self.paths_video:
            for y in x:
                tmp = y[:]
                tmp.reverse()
                for z in self.links:
                    if y == z.index:
                        z.flow_video_up += self.nodes[x[0][0]].flow_video

                        # Writing the name of path going through link
                        z.paths_video[str(x)] = self.nodes[x[0][0]].flow_video

                        break

                    elif tmp == z.index:
                        z.flow_video_down += self.nodes[x[0][0]].flow_video

                        # Writing the name of path going through link
                        z.paths_video[str(x)] = self.nodes[x[0][0]].flow_video

                        break

    def scatter_flow_be(self):

        for x in self.paths_be:
            for y in x:
                tmp = y[:]
                tmp.reverse()
                for z in self.links:
                    if y == z.index:
                        z.flow_be_up += self.nodes[x[0][0]].flow_be

                        # Writing the name of path going through link
                        z.paths_be[str(x)] = self.nodes[x[0][0]].flow_be

                        break

                    elif tmp == z.index:
                        z.flow_be_down += self.nodes[x[0][0]].flow_be

                        # Writing the name of path going through link
                        z.paths_be[str(x)] = self.nodes[x[0][0]].flow_be

                        break

    def sum_up_flow(self):
        for x in self.links:
            x.set_flow_voice()
            x.set_flow_video()
            x.set_flow_be()

    def scatter_iplr(self):
        for link in self.links:
            link.calculate_iplr(self.nodes)

    def sum_iplr_path_voice(self):

        # for link in self.links:
        #link.calculate_iplr(self.nodes)

        for path in self.paths_voice:
            self.iplr_for_paths_voice[str(path)] = 0
            tmp_iplr = 0
            for x in path:
                for y in self.links:
                    tmp = y.index[:]
                    tmp.reverse()
                    if y.index == x or tmp == x:
                        tmp_iplr += y.iplr_voice
                        break
            self.iplr_for_paths_voice[str(path)] = tmp_iplr

    def sum_iplr_path_video(self):

        # for link in self.links:
        #link.calculate_iplr(self.nodes)

        for path in self.paths_video:
            self.iplr_for_paths_video[str(path)] = 0
            tmp_iplr = 0
            for x in path:
                for y in self.links:
                    tmp = y.index[:]
                    tmp.reverse()
                    if y.index == x or tmp == x:
                        tmp_iplr += y.iplr_video
                        break
            self.iplr_for_paths_video[str(path)] = tmp_iplr

    def sum_iplr_path_be(self):

        # for link in self.links:
        #link.calculate_iplr(self.nodes)

        for path in self.paths_be:
            self.iplr_for_paths_be[str(path)] = 0
            tmp_iplr = 0
            for x in path:
                for y in self.links:
                    tmp = y.index[:]
                    tmp.reverse()
                    if y.index == x or tmp == x:
                        tmp_iplr += y.iplr_be
                        break
            self.iplr_for_paths_be[str(path)] = tmp_iplr

    def scatter_ipdt(self):
        for link in self.links:
            link.calculate_ipdt(self.nodes, 680, 8320, 12320)

    def sum_ipdt_path_voice(self):

        # for link in self.links:
        #    link.calculate_iplr(self.nodes)

        for path in self.paths_voice:
            self.ipdt_for_paths_voice[str(path)] = 0
            tmp_ipdt = 0
            for x in path:
                for y in self.links:
                    tmp = y.index[:]
                    tmp.reverse()
                    if y.index == x or tmp == x:
                        tmp_ipdt += y.ipdt_voice
                        break
            self.ipdt_for_paths_voice[str(path)] = tmp_ipdt

    def sum_ipdt_path_video(self):

        # for link in self.links:
        #    link.calculate_ipdt(self.nodes)

        for path in self.paths_video:
            self.ipdt_for_paths_video[str(path)] = 0
            tmp_ipdt = 0
            for x in path:
                for y in self.links:
                    tmp = y.index[:]
                    tmp.reverse()
                    if y.index == x or tmp == x:
                        tmp_ipdt += y.ipdt_video
                        break
            self.ipdt_for_paths_video[str(path)] = tmp_ipdt

    def sum_ipdt_path_be(self):

        # for link in self.links:
        #    link.calculate_ipdt(self.nodes)

        for path in self.paths_video:
            self.ipdt_for_paths_be[str(path)] = 0
            tmp_ipdt = 0
            for x in path:
                for y in self.links:
                    tmp = y.index[:]
                    tmp.reverse()
                    if y.index == x or tmp == x:
                        tmp_ipdt += y.ipdt_video
                        break
            self.ipdt_for_paths_be[str(path)] = tmp_ipdt

    def scatter_ipdv(self):
        for link in self.links:
            link.calculate_ipdv(self.nodes, 680, 8320, 12320)

    def sum_ipdv_path_voice(self):

        for path in self.paths_voice:
            self.ipdv_for_paths_voice[str(path)] = 0
            tmp_ipdv = 0
            for x in path:
                for y in self.links:
                    tmp = y.index[:]
                    tmp.reverse()
                    if y.index == x or tmp == x:
                        tmp_ipdv += y.ipdv_voice
                        break
            self.ipdv_for_paths_voice[str(path)] = tmp_ipdv

    def sum_ipdv_path_video(self):

        for path in self.paths_video:
            self.ipdv_for_paths_video[str(path)] = 0
            tmp_ipdv = 0
            for x in path:
                for y in self.links:
                    tmp = y.index[:]
                    tmp.reverse()
                    if y.index == x or tmp == x:
                        tmp_ipdv += y.ipdv_video
                        break
            self.ipdv_for_paths_video[str(path)] = tmp_ipdv

    def sum_ipdv_path_be(self):

        for path in self.paths_be:
            self.ipdv_for_paths_be[str(path)] = 0
            tmp_ipdv = 0
            for x in path:
                for y in self.links:
                    tmp = y.index[:]
                    tmp.reverse()
                    if y.index == x or tmp == x:
                        tmp_ipdv += y.ipdv_be
                        break
            self.ipdv_for_paths_be[str(path)] = tmp_ipdv


if __name__ == '__main__':

    d = Data()

    d.create_package_network(100, 1000, 1000)
    d.create_package_network(50, 500, 500)

    d.set_interest_matrix_voice([[0, 1], [1, 0]])
    d.set_interest_matrix_video([[0, 1], [1, 0]])
    d.set_interest_matrix_be([[0, 1], [1, 0]])

    d.process_data()

    d.create_node_edge(5, 15, 30)
    for x in range(4):
        d.create_node_core(5, 15, 30)
    d.create_node_edge(5, 15, 30)

    d.create_adjacency_matrix([[0, 1, 0, 1, 1, 0], [1, 0, 1, 1, 0, 0], [0, 1, 0, 1, 1, 1], [1, 1, 1, 0, 0, 0],
                               [1, 0, 1, 0, 0, 0], [0, 0, 1, 0, 0, 0]])

    print(d.adjacency_matrix)

    d.create_links()
    d.create_paths_matrix_voice()
    d.create_paths_matrix_video()
    d.create_paths_matrix_be()

    d.create_net_edge_matrix()
    d.set_connections()

    d.scatter_flow_voice()
    d.scatter_flow_video()
    d.scatter_flow_be()

    d.sum_up_flow()

    d.scatter_iplr()
    d.sum_iplr_path_voice()
    d.sum_iplr_path_video()
    d.sum_iplr_path_be()

    d.scatter_ipdt()
    d.sum_ipdt_path_voice()
    d.sum_ipdt_path_video()
    d.sum_ipdt_path_be()

    d.scatter_ipdv()
    d.sum_ipdv_path_voice()
    d.sum_ipdv_path_video()
    d.sum_ipdv_path_be()

    # for x in d.links:
    #   print(x.name)

    #d.delete_node(3)

    #for x in d.nodes:
    #   print(x.name)

    for x in d.links:
        print(x.index)
        print(x.flow_voice_up)
        print(x.flow_voice_down)
        print(x.flow_voice)
        print(x.paths_voice)
        print('-----------------------')
        print('IPLR for voice: ', x.iplr_voice)
        print('IPLR for video: ', x.iplr_video)
        print('IPLR for be: ', x.iplr_be)
        print('------------------------')
        print('IPDT for voice: ', x.ipdt_voice)
        print('IPDT for video: ', x.ipdt_video)
        print('IPDT for be: ', x.ipdt_be)
        print('+++++++++++++++++++++++')

    print('Voice IPLR: ', d.iplr_for_paths_voice)
    print('Video IPLR: ', d.iplr_for_paths_video)
    print('BE IPLR: ', d.iplr_for_paths_be)
    print('------------------------')
    print('Voice IPDT: ', d.ipdt_for_paths_voice)
    print('Video IPDT: ', d.ipdt_for_paths_video)
    print('BE IPDT: ', d.ipdt_for_paths_be)
    print('------------------------')
    print('Voice IPDV: ', d.ipdv_for_paths_voice)
    print('Video IPDV: ', d.ipdv_for_paths_video)
    print('BE IPDV: ', d.ipdv_for_paths_be)
    # print(d.connections)
    #print(d.connections_sliced)