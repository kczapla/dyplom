__author__ = 'perun'

import core.distribution as dist


if __name__ == '__main__':

    first_class = dist.Data()

    while True:
        print("""++++++++++OPTIONS++++++++++
                (1) - CREATE NETWORKS
                    (1.1) - CIRCUIT
                    (1.2) - PACKAGE
                (2) - CREATE INTEREST MATRIX
                    (2.1) - VOICE
                    (2.2) - VIDEO
                    (2.3) - BEST EFFORT
                (3) - CHANGE INTEREST MATRIX
                    (3.1) - VOICE
                    (3.2) - VIDEO
                    (3.3) - BEST EFFORT
                (4) - PROCESS DATA
                (5) - SHOW DATA
                (6) - USE TEST VALUES
                (7) - SHOW INTEREST MATRIX
                (8) - DELETE NETWORK
                (9) - EXIT PROGRAM
                ++++++++++OPTIONS+++++++++++""")
        what = str(input('Your choice: '))

        if '1.' in what:

                if what == '1.1':
                    intensity_voice = int(input('Intensity of voice stream: '))
                    loss = float(input('Loss probability: '))

                    if intensity_voice and loss:
                        first_class.create_circuit_network()
                    else:
                        print('Wrong values. Try again.')

                elif what == '1.2':
                    intensity_voice = int(input('Intensity of voice stream: '))
                    intensity_video = int(input('Instensity of video stream: '))
                    intensity_be = int(input('Intensity of be stream: '))

                    if not intensity_voice:
                        intensity_voice = 0
                    if not intensity_video:
                        intensity_video = 0
                    if not intensity_be:
                        intensity_be = 0

                    first_class.create_package_network(intensity_voice, intensity_video, intensity_be)
                else:
                    print("Błędna wartość. Spróbuj ponownie.")

        elif '2.' in what:
            if first_class.networks:
                if what == '2.1':
                    first_class.create_interest_matrix(first_class.interest_matrix_voice)
                elif what == '2.2':
                    first_class.create_interest_matrix(first_class.interest_matrix_video)
                elif what == '2.3':
                    first_class.create_interest_matrix(first_class.interest_matrix_be)
                else:
                    print('Wrong value! Choose from available options.')
                first_class.split_matrix()
            else:
                print('Wrong value! Choose from available options.')

        elif '3.' in what:
            if first_class.networks:
                row = str(input('Set row: '))
                col = str(input('Set column: '))
                if what == '3.1':
                    first_class.change_single_value_matrix(row, col, first_class.interest_matrix_voice)
                elif what == '3.2':
                    first_class.change_single_value_matrix(row, col, first_class.interest_matrix_video)
                elif what == '3.3':
                    first_class.change_single_value_matrix(row, col, first_class.interest_matrix_be)
                else:
                    print('Wrong value! Choose from available options.')
            else:
                print('Before operation create networks! Try again.')

        elif what == '4':
            if first_class.networks:
                first_class.process_data()
            else:
                print('Before process create networks! Try again.')

        elif what == '5':
            if first_class.networks:
                first_class.show_data()
            else:
                print('Before operation create networks! Try again.')

        elif what == '6':
            first_class.use_test_values()

        elif what == '7':
            if first_class.networks:
                print(first_class.interest_matrix_voice)
                print(first_class.interest_matrix_video)
                print(first_class.interest_matrix_be)
            else:
                print('Before operation create networks! Try again.')

        elif what == '8':
            if first_class.networks:
                first_class.delete_network(int(input('Podaj indeks sieci, którą chcesz usunąć: ')))
            else:
                print('Before operation create networks! Try again.')

        elif what == '9':
            print('EXIT PROGRAM')
            break