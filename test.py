__author__ = 'perun'


def test(codec='ikso'):
    print(codec)

if __name__ == '__main__':

    while True:
        x = str(input('hwdp: '))
        if not x:
            print('Zła wartość')
        else:
            test()


