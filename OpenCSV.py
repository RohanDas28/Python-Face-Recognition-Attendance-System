import tkinter as tk
import csv
from tkinter import ttk
from tkinter import filedialog


class CSVTable(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # Table
        self.table = ttk.Treeview(self, columns=('column1', 'column2'), show='headings')
        self.table.heading('column1', text='Name')
        self.table.heading('column2', text='Time')
        self.table.grid(row=0, column=0, padx=5, pady=5)

        # Open file button
        self.open_file_button = tk.Button(self, text='Open File', command=self.open_file)
        self.open_file_button.grid(row=1, column=0, padx=5, pady=5)

    def open_file(self):
        file_path = tk.filedialog.askopenfilename()
        if file_path:
            with open(file_path, newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=',', quotechar='"')
                for row in reader:
                    self.table.insert('', tk.END, values=row)

root = tk.Tk()
root.title('Checking Attendance')
app = CSVTable(master=root)
app.mainloop()
