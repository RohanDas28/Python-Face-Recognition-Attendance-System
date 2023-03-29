import tkinter as tk
from tkinter import filedialog
import json

class FaceImageEntry(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # Name label and entry
        self.name_label = tk.Label(self, text="Name:", font=("Arial", 14))
        self.name_label.grid(row=0, column=0, padx=10, pady=10)
        self.name_entry = tk.Entry(self, font=("Arial", 14))
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        # File path label and entry
        self.file_label = tk.Label(self, text="File Path:", font=("Arial", 14))
        self.file_label.grid(row=1, column=0, padx=10, pady=10)
        self.file_entry = tk.Entry(self, state='readonly', font=("Arial", 14))
        self.file_entry.grid(row=1, column=1, padx=10, pady=10)
        self.browse_button = tk.Button(self, text="Browse", font=("Arial", 14), command=self.browse_file)
        self.browse_button.grid(row=1, column=2, padx=10, pady=10)

        # Add button
        self.add_button = tk.Button(self, text="Add", font=("Arial", 16, "bold"), bg="green", fg="white", command=self.add_entry)
        self.add_button.grid(row=2, column=1, padx=10, pady=20)

    def browse_file(self):
        file_path = filedialog.askopenfilename()
        self.file_entry.configure(state='normal')
        self.file_entry.delete(0, tk.END)
        self.file_entry.insert(0, file_path)
        self.file_entry.configure(state='readonly')

    def add_entry(self):
        name = self.name_entry.get()
        file_path = self.file_entry.get()
        if name and file_path:
            # Load existing face images from file
            with open('face_images.json') as f:
                face_images = json.load(f)['faces']

            # Append new entry to the face images list
            new_entry = {"name": name, "file_path": file_path}
            face_images.append(new_entry)

            # Write updated face images list to file
            with open('face_images.json', 'w') as f:
                json.dump({'faces': face_images}, f)

            # Clear input fields
            self.name_entry.delete(0, tk.END)
            self.file_entry.configure(state='normal')
            self.file_entry.delete(0, tk.END)
            self.file_entry.configure(state='readonly')

            print(f"Added {new_entry} to face_images.json")
        else:
            print("Please enter a name and file path")

root = tk.Tk()
root.title("Students Entry")
root.geometry("500x200")
app = FaceImageEntry(master=root)
app.mainloop()
