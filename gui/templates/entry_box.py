__author__ = 'perun'

import core.distribution
import tkinter as tk
import tkinter.messagebox


class EntryRow(tk.Frame):
    def __init__(self, parent):

        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.pack(side=tk.TOP, pady=2)

        self.row = tk.Frame(self)
        self.row.pack(side=tk.TOP)

        self.entries = [tk.StringVar(), tk.StringVar()]

        self.make_entry_row(self.row, self.entries)

    def make_entry_row(self, row, entries):

        for entry in entries:
            tk.Entry(row, textvariable=entry, width=2, justify=tk.RIGHT).pack(side=tk.LEFT, padx=1)

        tk.Button(row, text='+', command=lambda: self.add_entry(row, entries)).pack(side=tk.LEFT, padx=1)
        tk.Button(row, text='-', command=lambda: self.subtract_entry(row, entries)).pack(side=tk.LEFT, padx=1)
        tk.Button(row, text='X', command=self.destroy).pack(side=tk.LEFT, padx=1)

    def add_entry(self, row, entries):

        ent = tk.StringVar()
        entries.append(ent)

        row.destroy()
        row = tk.Frame(self)
        row.pack(side=tk.TOP)

        self.make_entry_row(row, entries)

    def subtract_entry(self, row, entries):

        if len(entries) > 2:
            entries.pop()
        else:
            tkinter.messagebox.showinfo('Info', 'Path length has to be at least 2 nodes...')

        row.destroy()
        row = tk.Frame(self)
        row.pack(side=tk.TOP)

        self.make_entry_row(row, entries)

    def fetch_values(self):

        try:
            tmp = [int(ent.get()) for ent in self.entries]
            return tmp
        except ValueError:
            tkinter.messagebox.showerror('Error', 'Insert only digits! Try again...')


class EntryFrame(tk.Frame):
    def __init__(self, parent, distribution):
        tk.Frame.__init__(self, parent)

        self.parent = parent
        parent.title('Create paths')
        self.pack(side=tk.TOP)

        # self.distribution = distribution

        self.rows_frame = tk.Frame(self)
        self.rows_frame.pack(side=tk.TOP)

        self.rows = [EntryRow(self.rows_frame)]

        self.make_control_panel(self.rows, distribution)

    def make_control_panel(self, rows, distribution):

        row = tk.Frame(self, relief=tk.SUNKEN, bd=1)
        row.pack(side=tk.BOTTOM, pady=20)

        both_directions = tk.IntVar()

        tk.Checkbutton(row, text='Both directions paths', variable=both_directions).pack(side=tk.LEFT, padx=10, pady=5)

        tk.Button(row, text='Submit', command=lambda: self.fetch_rows(rows, distribution, both_directions)).pack(
            side=tk.LEFT, padx=10, pady=5)
        tk.Button(row, text='Add path', command=lambda: self.add_row(rows)).pack(side=tk.LEFT, padx=10)
        tk.Button(row, text='Close', command=self.parent.destroy).pack(side=tk.LEFT, padx=10)

    def add_row(self, rows):

        row = EntryRow(self.rows_frame)
        rows.append(row)

    def fetch_rows(self, rows, distribution, directions):

        paths = [path.fetch_values() for path in rows]

        if self.check_if_repeat(paths):
            tkinter.messagebox.showerror('Error', 'Paths sequence repeating!')
        else:
            print('Paths ok...')

            if directions.get():

                print('Both...')
                reversed_paths = paths[:]

                for path in reversed_paths:
                    tmp = path[:]
                    tmp.reverse()
                    paths.append(tmp)

                distribution.create_paths_matrix(paths)

            else:
                distribution.create_paths_matrix(paths)

    def not_ready(self):
        print('Not ready...')

    def check_if_repeat(self, element):

        for i in range(0, len(element)):
            for j in range(i + 1, len(element)):
                if element[i] == element[j]:
                    print(j)
                    return True
        return False


if __name__ == '__main__':
    root = tk.Tk()

    d = core.distribution.Data()

    x = EntryFrame(tk.Toplevel(root), d)
    root.mainloop()