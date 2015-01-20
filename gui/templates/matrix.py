__author__ = 'perun'


from tkinter import *
from tkinter.messagebox import *
import core.distribution as distribution


class Matrix(Frame):
    def __init__(self, distribution, size, tittle='Matrix', parent=None, **extras):
        Frame.__init__(self, parent, **extras)
        self.parent = parent
        self.parent.title('Matrix maker')
        self.distribution = distribution
        self.pack(side=TOP)

        self.matrix = []
        self.tittle = tittle
        self.buttons_fields = [['Ok', self.fetch], ['Cancel', self.parent.destroy]]

        self.make_matrix(size)
        self.make_buttons()

        self.focus_set()          # take over input focus,
        self.grab_set()           # disable other windows while I'm open,
        self.wait_window()        # and wait here until win destroyed

    def make_matrix(self, size):
        Label(self, text='Create '+self.tittle).pack(side=TOP)
        for x in range(size):
            entry = []
            row = Frame(self)
            row.pack(side=TOP)
            for y in range(size):
                ent = Entry(row, width=5)
                ent.pack(side=LEFT, padx=1, pady=1)
                entry.append(ent)
            self.matrix.append(entry)

    def make_buttons(self):
        row = Frame(self)
        row.pack(side=TOP, fill=X, pady=5)
        Button(row, text='Ok', command=self.fetch).pack(side=LEFT, expand=YES, fill=X, padx=5)
        Button(row, text='Cancel', command=self.parent.destroy).pack(side=RIGHT, expand=YES, fill=X, padx=5)

    def fetch(self):
        zzz = [[float(y.get()) for y in x] for x in self.matrix]
        #self.distribution.interest_matrix_voice = [[float(y.get()) for y in x] for x in self.matrix]
        print(zzz)


class ShowMatrixAdjacency(Matrix):
    def make_matrix(self, size):
        Label(self, text='Show '+self.tittle).pack(side=TOP)
        for vector in self.distribution.adjacency_matrix:
            row = Frame(self)
            row.pack(side=TOP)
            for cell in vector:
                x = StringVar()
                x.set(cell)
                ent = Entry(row, width=5, state='readonly', textvariable=x)
                ent.pack(side=LEFT, padx=1, pady=1)

    def make_buttons(self):
        row = Frame(self)
        row.pack(side=TOP, fill=X, pady=5)
        Button(row, text='Cancel', command=self.parent.destroy).pack(side=RIGHT, expand=YES, fill=X, padx=5)


class ShowMatrixVoiceInterest(Matrix):
    def make_matrix(self, size):
        Label(self, text='Show '+self.tittle).pack(side=TOP)
        for vector in self.distribution.interest_matrix_voice:
            row = Frame(self)
            row.pack(side=TOP)
            for cell in vector:
                x = StringVar()
                x.set(cell)
                ent = Entry(row, width=5, state='readonly', textvariable=x)
                ent.pack(side=LEFT, padx=1, pady=1)

    def make_buttons(self):
        row = Frame(self)
        row.pack(side=TOP, fill=X, pady=5)
        Button(row, text='Cancel', command=self.parent.destroy).pack(side=RIGHT, expand=YES, fill=X, padx=5)


class ShowMatrixVideoInterest(Matrix):
    def make_matrix(self, size):
        Label(self, text='Show '+self.tittle).pack(side=TOP)
        for vector in self.distribution.interest_matrix_video:
            row = Frame(self)
            row.pack(side=TOP)
            for cell in vector:
                x = StringVar()
                x.set(cell)
                ent = Entry(row, width=5, state='readonly', textvariable=x)
                ent.pack(side=LEFT, padx=1, pady=1)

    def make_buttons(self):
        row = Frame(self)
        row.pack(side=TOP, fill=X, pady=5)
        Button(row, text='Cancel', command=self.parent.destroy).pack(side=RIGHT, expand=YES, fill=X, padx=5)


class ShowMatrixBeInterest(Matrix):
    def make_matrix(self, size):
        Label(self, text='Show '+self.tittle).pack(side=TOP)
        for vector in self.distribution.interest_matrix_be:
            row = Frame(self)
            row.pack(side=TOP)
            for cell in vector:
                x = StringVar()
                x.set(cell)
                ent = Entry(row, width=5, state='readonly', textvariable=x)
                ent.pack(side=LEFT, padx=1, pady=1)

    def make_buttons(self):
        row = Frame(self)
        row.pack(side=TOP, fill=X, pady=5)
        Button(row, text='Cancel', command=self.parent.destroy).pack(side=RIGHT, expand=YES, fill=X, padx=5)


class MatrixVoiceInterest(Matrix):
    def fetch(self):
        if self.matrix[0][0].get():
            self.distribution.interest_matrix_voice = [[float(y.get()) for y in x] for x in self.matrix]
            #print(self.distribution.interest_matrix_be)
            print('Voice matrix created.')
            self.parent.destroy()
        else:
            print('Nothing inserted into voice matrix\'s entries.')
            showinfo('Info', 'Nothing inserted into voice interest matrix\'s entries.')
            #self.parent.destroy()


class MatrixVideoInterest(Matrix):
    def fetch(self):
        if self.matrix[0][0].get():
            self.distribution.interest_matrix_video = [[float(y.get()) for y in x] for x in self.matrix]
            #print(self.distribution.interest_matrix_be)
            print('Video matrix created.')
            self.parent.destroy()
        else:
            showinfo('Info', 'Nothing inserted into video interest matrix\'s entries.')
            print('Nothing inserted into video matrix\'s entries.')
            #self.parent.destroy()


class MatrixBeInterest(Matrix):
    def fetch(self):
        if self.matrix[0][0].get():
            self.distribution.interest_matrix_be = [[float(y.get()) for y in x] for x in self.matrix]
            #print(self.distribution.interest_matrix_be)
            print('BE matrix created.')
            self.parent.destroy()
        else:
            showinfo('Info', 'Nothing inserted into Be interest matrix\'s entries.')
            print('Nothing inserted into BE matrix\'s entries.')
            #self.parent.destroy()


class MatrixAdjacency(Matrix):
    def fetch(self):
        if self.matrix[0][0].get():
            matrix = [[float(y.get()) for y in x] for x in self.matrix]
            self.distribution.create_adjacency_matrix(matrix)
            #print(self.distribution.interest_matrix_be)
            print('Adjacency matrix created...')
            self.parent.destroy()
        else:
            showinfo('Info', 'Nothing inserted into Adjacency matrix\'s entries.')
            print('Nothing inserted into Adjacency matrix\'s entries.')
            #self.parent.destroy()


class NetEdgeMatrix(Matrix):
    def make_matrix(self, size):
        Label(self, text='Create '+self.tittle).pack(side=TOP)
        fields = [(network.name, network.index) for network in self.distribution.networks]
        for field in fields:
            row = Frame(self)
            row.pack(side=TOP)
            Label(row, text=field[0], width=20).pack(side=LEFT, padx=5)
            ent1_variable = StringVar()
            ent1_variable.set(field[1])
            ent1 = Entry(row, width=5, state='disabled', textvariable=ent1_variable)
            ent2 = Entry(row, width=5)
            ent1.pack(side=LEFT, padx=2)
            #ent1.insert(0, field[0])
            ent2.pack(side=LEFT, padx=2)

            self.matrix.append([ent1, ent2])

            #tpl.entry(row, LEFT, tmp, width=5, state='disabled')
            #ent2 = tpl.entry(row, LEFT, 'Index of edge router', width=25)

            #self.matrix.append([tpl.entry(row, LEFT, tmp, width=5, state='disabled'),
             #                   tpl.entry(row, LEFT, 'Index of edge router', width=25)])

    def fetch(self):
        if self.matrix[0][0].get():
            #self.distribution.net_edge = [[int(y.get()) for y in x] for x in self.matrix]
            paths = []
            stop = False
            for x, y in self.matrix:
                if int(y.get()) <= self.distribution.index_nodes:
                    paths.append([int(x.get()), int(y.get())])
                else:
                    showerror('Error', 'Node with index {} doesn\'t exists. Insert correct values.'
                              .format(int(y.get())))
                    stop = True
                    break

            if not stop:
                self.distribution.create_net_edge_matrix(paths)
                print(paths)
                print('Net - edge matrix created.')

            self.parent.destroy()
        else:
            showinfo('Info', 'Nothing inserted into Net - edge matrix\'s entries.')
            print('Nothing inserted into Net - edge matrix\'s entries.')
            #self.parent.destroy()


class CreatePaths(Matrix):
    def make_matrix(self, size):
         Label(self, text='Create '+self.tittle).pack(side=TOP)

if __name__ == "__main__":
        root = Tk()
        d = distribution.Data()
        d.test()
        m = NetEdgeMatrix(d, 2, 'IKSO', root)
        root.mainloop()