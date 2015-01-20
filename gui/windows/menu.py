__author__ = 'perun'

from tkinter import *
from tkinter.messagebox import *

import core.distribution as distribution
import gui.templates.quitter as quitter
import gui.templates.widgets as tpl
import gui.windows.popups as popups
import gui.templates.show as show
import gui.templates.matrix


class MenuFrame(Frame):
    def __init__(self, distribution, parent=None, **extras):
        Frame.__init__(self, parent, **extras)
        self.pack(side=TOP, **extras)

        self.parent = parent
        self.distribution = distribution
        self.file_saver = popups.ChooseFile(self.parent)

        self.make_content()

    def make_content(self):

        self.make_top_menu_bar(self.parent)

        menu_box = Frame(self, relief=SUNKEN, bd=1)
        menu_box.pack(side=LEFT, padx=5, pady=5)
        tpl.label(menu_box, TOP, 'MENU')
        tpl.button(menu_box, TOP, 'Create network', lambda: popups.ChooseNetwork(self.distribution,
                                                                                 Toplevel(self))).pack(pady=5, padx=5)
        tpl.button(menu_box, TOP, 'Create node', lambda: popups.ChooseNode(self.distribution,
                                                                           Toplevel(self))).pack(pady=5, padx=5)
        tpl.button(menu_box, TOP, 'Create matrix', self.chose_matrix).pack(pady=5, padx=5)
        tpl.button(menu_box, TOP, 'Show data', self.show_data).pack(pady=5, padx=5)
        tpl.button(menu_box, TOP, 'Process data', self.process_data).pack(pady=5, padx=5)

        quitter.Quitter(menu_box)

        log_box = Frame(self, relief=SUNKEN, bd=1)
        log_box.pack(side=LEFT, padx=5, pady=5)
        show.LogBox(log_box)

    def chose_matrix(self):
        popups.CreateMatrix(self.distribution,
                            Toplevel(self))

    def show_data(self):
        if self.distribution.index_networks:
            popups.ShowData(self.distribution, Toplevel(self))
        else:
            showwarning('Warning', 'Networks don\'t exist. Create networks first to use this option.')

    def process_data(self):
        if self.distribution.index_networks:
            popups.ChooseData(self.distribution, Toplevel(self))
        else:
            showwarning('Warning', 'Networks don\'t exist. Create networks first to use this option.')

    def make_top_menu_bar(self, win):

        top = Menu(win)

        file = Menu(top)
        file.add_command(label='New...', command=self.new_project, underline=0)
        file.add_command(label='Save as...', command=self.save_file, underline=0)
        file.add_command(label='Open...', command=self.load_file, underline=0)
        file.add_command(label='Exit', command=self.parent.destroy, underline=0)
        top.add_cascade(label='File', menu=file, underline=0)

        networks = Menu(top)
        #networks.add_command(label='Show...', command=self.not_ready, underline=0)

        matrixes = Menu(networks)

        interest = Menu(matrixes)
        interest.add_command(label='Voice', command=self.show_interest_marix_voice, underline=0)
        interest.add_command(label='Video', command=self.show_interest_marix_video, underline=0)
        interest.add_command(label='BE', command=self.show_interest_marix_be, underline=0)
        matrixes.add_cascade(label='Interest matrix...', menu=interest, underline=0)
        matrixes.add_command(label='Adjacency...', command=self.show_adjacency_matrix, underline=0)

        matrixes.add_command(label='Paths...', command=self.not_ready, underline=0)
        matrixes.add_separator()

        qos = Menu(matrixes)
        qos.add_command(label='Voice', command=self.show_qos_voice)
        qos.add_command(label='Video', command=self.show_qos_video)
        qos.add_command(label='BE', command=self.show_qos_be)
        matrixes.add_cascade(label='Qos in paths...', menu=qos)


        networks.add_cascade(label='Show...', menu=matrixes, underline=0)
        networks.add_command(label='Set...', command=self.not_ready, underline=0)

        top.add_cascade(label='Global', menu=networks, underline=0)

        help_menu = Menu(win)
        help_menu.add_command(label='About', command=self.not_ready, underline=0)
        top.add_cascade(label='Help', menu=help_menu, underline=0)

        win.config(menu=top)

    def not_ready(self):
        showinfo('Info', 'Option is not ready.')

    def save_file(self):
        self.file_saver.save_file(self.distribution)

    def load_file(self):
        self.distribution = self.file_saver.load_file()

    def new_project(self):
        print('Creating new project...')
        self.distribution = distribution.Data()

    def show_interest_marix_voice(self):
        if self.distribution.interest_matrix_voice:
            gui.templates.matrix.ShowMatrixVoiceInterest(self.distribution, self.distribution.index_networks, 'Voice',
                                                         Toplevel())
        else:
            showerror('Error', 'Voice matrix has been not created...')

    def show_interest_marix_video(self):
        if self.distribution.interest_matrix_video:
            gui.templates.matrix.ShowMatrixVideoInterest(self.distribution, self.distribution.index_networks, 'Video',
                                                         Toplevel())
        else:
            showerror('Error', 'Video matrix has been not created...')

    def show_interest_marix_be(self):
        if self.distribution.interest_matrix_be:
            gui.templates.matrix.ShowMatrixBeInterest(self.distribution, self.distribution.index_networks, 'BE',
                                                      Toplevel())
        else:
            showerror('Error', 'BE matrix has been not created...')

    def show_adjacency_matrix(self):
        if self.distribution.adjacency_matrix:
            gui.templates.matrix.ShowMatrixAdjacency(self.distribution, self.distribution.index_nodes, 'Adjacency',
                                                     Toplevel())
        else:
            showerror('Error', 'Adjacency matrix has been not created...')

    def show_qos_voice(self):
        parent = Toplevel()
        parent.title('QoS voice')
        main_frame = Frame(parent)
        main_frame.pack(side=TOP)

        iplr_frame = Frame(main_frame, relief=SUNKEN, bd=1, padx=5)
        iplr_frame.pack(side=LEFT)

        ipdt_frame = Frame(main_frame, relief=SUNKEN, bd=1, padx=5)
        ipdt_frame.pack(side=LEFT)

        ipdv_frame = Frame(main_frame, relief=SUNKEN, bd=1, padx=5)
        ipdv_frame.pack(side=LEFT)

        row = Frame(iplr_frame)
        row.pack(side=TOP)

        Label(row, text='IPLR').pack(side=LEFT)

        i = 1
        for path in self.distribution.iplr_for_paths_voice:
            row = Frame(iplr_frame)
            row.pack(side=TOP)
            path_name = '{}. {}'.format(str(i), path)
            Label(row, text=path_name).pack(side=LEFT)
            tmp = StringVar()
            tmp.set(self.distribution.iplr_for_paths_voice[path])
            Entry(row, textvariable=tmp, state='disabled', width=25).pack(side=LEFT)
            i += 1

        row = Frame(ipdt_frame)
        row.pack(side=TOP)

        Label(row, text='IPDT').pack(side=LEFT)

        i = 1
        for path in self.distribution.ipdt_for_paths_voice:
            row = Frame(ipdt_frame)
            row.pack(side=TOP)
            path_name = '{}. {} {}'.format(str(i), path, '[s]')
            Label(row, text=path_name).pack(side=LEFT)
            tmp = StringVar()
            tmp.set(self.distribution.ipdt_for_paths_voice[path])
            Entry(row, textvariable=tmp, state='disabled', width=25).pack(side=LEFT)
            i += 1

        row = Frame(ipdv_frame)
        row.pack(side=TOP)

        Label(row, text='IPDV').pack(side=LEFT)

        i = 1
        for path in self.distribution.ipdt_for_paths_voice:
            row = Frame(ipdv_frame)
            row.pack(side=TOP)
            path_name = '{}. {} {}'.format(str(i), path, '[s]')
            Label(row, text=path_name).pack(side=LEFT)
            tmp = StringVar()
            tmp.set(self.distribution.ipdv_for_paths_voice[path])
            Entry(row, textvariable=tmp, state='disabled', width=25).pack(side=LEFT)
            i += 1

        row = Frame(parent)
        row.pack(side=TOP)
        Button(row, text='Close', command=parent.destroy).pack(side=LEFT)

    def show_qos_video(self):
        parent = Toplevel()
        parent.title('QoS video')
        main_frame = Frame(parent)
        main_frame.pack(side=TOP)

        iplr_frame = Frame(main_frame, relief=SUNKEN, bd=1, padx=5)
        iplr_frame.pack(side=LEFT)

        ipdt_frame = Frame(main_frame, relief=SUNKEN, bd=1, padx=5)
        ipdt_frame.pack(side=LEFT)

        ipdv_frame = Frame(main_frame, relief=SUNKEN, bd=1, padx=5)
        ipdv_frame.pack(side=LEFT)

        row = Frame(iplr_frame)
        row.pack(side=TOP)

        Label(row, text='IPLR').pack(side=LEFT)

        i = 1
        for path in self.distribution.iplr_for_paths_video:
            row = Frame(iplr_frame)
            row.pack(side=TOP)
            path_name = '{}. {}'.format(str(i), path)
            Label(row, text=path_name).pack(side=LEFT)
            tmp = StringVar()
            tmp.set(self.distribution.iplr_for_paths_video[path])
            Entry(row, textvariable=tmp, state='disabled', width=25).pack(side=LEFT)
            i += 1

        row = Frame(ipdt_frame)
        row.pack(side=TOP)

        Label(row, text='IPDT').pack(side=LEFT)

        i = 1
        for path in self.distribution.ipdt_for_paths_video:
            row = Frame(ipdt_frame)
            row.pack(side=TOP)
            path_name = '{}. {} {}'.format(str(i), path, '[s]')
            Label(row, text=path_name).pack(side=LEFT)
            tmp = StringVar()
            tmp.set(self.distribution.ipdt_for_paths_video[path])
            Entry(row, textvariable=tmp, state='disabled', width=25).pack(side=LEFT)
            i += 1

        row = Frame(ipdv_frame)
        row.pack(side=TOP)

        Label(row, text='IPDV').pack(side=LEFT)

        i = 1
        for path in self.distribution.ipdt_for_paths_video:
            row = Frame(ipdv_frame)
            row.pack(side=TOP)
            path_name = '{}. {} {}'.format(str(i), path, '[s]')
            Label(row, text=path_name).pack(side=LEFT)
            tmp = StringVar()
            tmp.set(self.distribution.ipdv_for_paths_video[path])
            Entry(row, textvariable=tmp, state='disabled', width=25).pack(side=LEFT)
            i += 1

        row = Frame(parent)
        row.pack(side=TOP)
        Button(row, text='Close', command=parent.destroy).pack(side=LEFT)

    def show_qos_be(self):
        parent = Toplevel()
        parent.title('QoS BE')
        main_frame = Frame(parent)
        main_frame.pack(side=TOP)

        iplr_frame = Frame(main_frame, relief=SUNKEN, bd=1, padx=5)
        iplr_frame.pack(side=LEFT)

        ipdt_frame = Frame(main_frame, relief=SUNKEN, bd=1, padx=5)
        ipdt_frame.pack(side=LEFT)

        ipdv_frame = Frame(main_frame, relief=SUNKEN, bd=1, padx=5)
        ipdv_frame.pack(side=LEFT)

        row = Frame(iplr_frame)
        row.pack(side=TOP)

        Label(row, text='IPLR').pack(side=LEFT)

        i = 1
        for path in self.distribution.iplr_for_paths_be:
            row = Frame(iplr_frame)
            row.pack(side=TOP)
            path_name = '{}. {}'.format(str(i), path)
            Label(row, text=path_name).pack(side=LEFT)
            tmp = StringVar()
            tmp.set(self.distribution.iplr_for_paths_be[path])
            Entry(row, textvariable=tmp, state='disabled', width=25).pack(side=LEFT)
            i += 1

        row = Frame(ipdt_frame)
        row.pack(side=TOP)

        Label(row, text='IPDT').pack(side=LEFT)

        i = 1
        for path in self.distribution.ipdt_for_paths_be:
            row = Frame(ipdt_frame)
            row.pack(side=TOP)
            path_name = '{}. {} {}'.format(str(i), path, '[s]')
            Label(row, text=path_name).pack(side=LEFT)
            tmp = StringVar()
            tmp.set(self.distribution.ipdt_for_paths_be[path])
            Entry(row, textvariable=tmp, state='disabled', width=25).pack(side=LEFT)
            i += 1

        row = Frame(ipdv_frame)
        row.pack(side=TOP)

        Label(row, text='IPDV').pack(side=LEFT)

        i = 1
        for path in self.distribution.ipdt_for_paths_be:
            row = Frame(ipdv_frame)
            row.pack(side=TOP)
            path_name = '{}. {} {}'.format(str(i), path, '[s]')
            Label(row, text=path_name).pack(side=LEFT)
            tmp = StringVar()
            tmp.set(self.distribution.ipdv_for_paths_be[path])
            Entry(row, textvariable=tmp, state='disabled', width=25).pack(side=LEFT)
            i += 1

        row = Frame(parent)
        row.pack(side=TOP)
        Button(row, text='Close', command=parent.destroy).pack(side=LEFT)


if __name__ == '__main__':

    root = Tk()
    d = distribution.Data()
    d.test()
    m = MenuFrame(d, root)

    m.pack()
    root.mainloop()