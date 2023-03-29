import tkinter as tk
import subprocess

def open_attendance():
    global status
    status.set('Opening attendance...')
    subprocess.call(['python', 'attendance_system.py'])
    status.set('Ready')

def check_attendance():
    global status
    status.set('Checking attendance...')
    subprocess.call(['python', 'OpenCSV.py'])
    status.set('Ready')

def add_students():
    global status
    status.set('Opening add students')
    subprocess.call(['python', 'AddStudent.py'])
    status.set('Ready')

root = tk.Tk()
root.title('Attendance System V1.0 by Rohan')
root.geometry('640x360')
root.resizable(False, False)

status = tk.StringVar()
status.set('')

# Add welcome label
welcome_label = tk.Label(root, text='Welcome to Attendance System V1.0 by Rohan!\nHere are the things you can do:', font=('Arial', 20, 'bold'), fg='#6C3483')
welcome_label.pack(expand=True)

# Add button frame
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

# Add attendance button
attendance_button = tk.Button(button_frame, text='Open Attendance', width=15, height=2, bg='#FFB6C1', font=('Arial', 12, 'bold'), command=open_attendance)
attendance_button.pack(side=tk.LEFT, padx=10)

# Add check attendance button
check_attendance_button = tk.Button(button_frame, text='Check Attendance', width=15, height=2, bg='#98FB98', font=('Arial', 12, 'bold'), command=check_attendance)
check_attendance_button.pack(side=tk.LEFT, padx=10)

# Add add students button
getting_out_button = tk.Button(button_frame, text='Add Students', width=15, height=2, bg='#87CEFA', font=('Arial', 12, 'bold'), command=add_students)
getting_out_button.pack(side=tk.LEFT, padx=10)

root.mainloop()
