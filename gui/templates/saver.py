__author__ = 'perun'

import pickle


class FileSaver(object):
    def save_object(self, instance, file_path, protocol=pickle.HIGHEST_PROTOCOL):
        with open(file_path, 'wb') as file:
            print('Saving project in to the file from the path: ', file.name)
            pickle.Pickler(file, protocol).dump(instance)

    def load_object(self, file_path):
        with open(file_path, 'rb') as file:
            print('Loading project from the file from the path: ', file.name)
            return pickle.Unpickler(file).load()


class Name(object):
    def __init__(self, name, surrname):
        self.name = name
        self.surrname = surrname

if __name__ == '__main__':

    #x = Name('Adam', 'Nadolny')
    #FileSaver().save_object(x, 'C:\\Users\\Public\\test.txt')
    x = FileSaver().load_object('C:\\Users\\Public\\test.txt')
    print(x.name)