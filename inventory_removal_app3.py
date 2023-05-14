from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter as tk
import os
from tkinter import messagebox
import subprocess

from pyparsing import col


def input_source():
    input_path = tk.filedialog.askdirectory()
    input_entry.delete(1, tk.END)  # Remove current text in entry
    input_entry.insert(0, input_path)  # Insert the 'path'
    

def delete():
    files = (text_box.get('1.0', END))
    f_name = str(files.split('\n'))
    f_name2 = files.split('\n')
    f_suffix = ex_cb1.get()
    f_path = input_entry.get()
    dir_files = f_path.replace('/', '\\')
    for file in f_name2:
        try:
            if text_box.compare("end-1c", "==", "1.0"):
                print("the widget is empty")# If text box has nothing in it, print the declared statement.
            else:
                os.chdir(dir_files)
                full_file = dir_files + str(file + f_suffix)
                full_file2 = str(file + f_suffix)
                print(full_file2)
                os.remove(full_file2)
        except FileNotFoundError as e:
            print('File Does Not Exist')       
    text_box.delete('1.0', END)
    messagebox.showinfo(title='INFO MESSAGE', message='Files Have Been Deleted')
    
         

root=Tk()
root.geometry('500x500')
root.title('INVENTORY REMOVAL')
root.config(background='#615f5f')


def open_aboutFile():
    print('About')
    about_win = Toplevel(root)
    about_win.title('ABOUT APPLICATION')
    about_win.geometry('600x350')
    about_win.config(background='#615f5f')
    about_label = Label(about_win, text='HOW TO OPERATE APPLICATION:\n\n\n\n1. Click button "Add File Path" and select which directory the files are in.\n\n2. Copy and paste filenames in the text box.\n\n3. Click the "Delete" button to delete the desired files.\n\n\n\nCopyright © 2022 LOUIS C. TURNDICK III\n\nLicensed: Public Domain\n\nlouisturndickiii@gmail.com',
                        bg='#615f5f', fg='#fffdfc', font=(8), pady=20).pack()


menubar = Menu(root)
root.config(menu=menubar)

about_app = Menu(menubar, tearoff=0, font=("Arial", 8))
menubar.add_command(label="About", command=open_aboutFile)

input_entry = tk.Entry(root, text="", width=40)
input_entry.grid(row=2, column=1, pady=10, padx=10, ipadx=10)


browse1 = tk.Button(root, text="Add File Path", command=input_source)
browse1.grid(row=3, column=0, pady=10, padx=10, ipadx=10)


delete_button = Button(root,text="Delete",command=delete)
delete_button.grid(row=5, column=0, pady=0, padx=10, ipadx=10)

input_label = Label(root, text='Copy Filenames Into Text Box',
                    bg='#615f5f', fg='#fffdfc', font=(12))
input_label.grid(row=3, column=1, pady=10, padx=10,
                 ipadx=10)


# MAIN TEXT WINDOW - Used to add program names to search for
text_box = Text(root,
            height=20,
            width=40)
text_box.grid(row=4, column=1, pady=10, padx=10, ipadx=10)

extensions = ['.avi', '.docx', '.mp4', '.mpg', '.mpeg', '.mxf', 
'.txt', '.mp2', '.mpv', '.ogg', '.wmv', '.flv', 
'.mkv']
ex_cb1 = ttk.Combobox(root, values=extensions, width=10)
ex_cb1.grid(row=4, column=0, pady=10, padx=10, ipadx=10)

root.mainloop()