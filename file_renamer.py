from zipfile import ZipFile
import os
import shutil
import tkinter as tk
from tkinter import filedialog


def unzip(file,dest):
    try:
        with ZipFile(file, 'r') as zipped:
            zipped.extractall(dest)
    except:
        print("Zip file error")

def rename_files(directory):
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            new_name = file_name[9:]
            os.rename(f'{directory}/{file_name}',f'{directory}/{new_name}')

def add_file(file,directory):
    for root, dirs, files in os.walk(directory):
        dot = file.find(".")
        new_ext = file[dot:]
        
        for filename in files:
            dot = filename.find("-")
            new_filename = f'{filename[:dot]} Criteria{new_ext}'
            shutil.copyfile(file,f'{directory}/{new_filename}')

def zip_btn_click():
    root.zipped_file = filedialog.askopenfilename(initialdir=".")
    print(root.zipped_file)

def dest_btn_click():
    root.destination = filedialog.askdirectory(initialdir=".")
    print(root.destination)

def crit_btn_click():
    root.criteria = filedialog.askopenfilename(initialdir=".")
    print(root.criteria)

def go_btn_click():
    unzip(root.zipped_file, root.destination)
    rename_files(root.destination)
    add_file(root.criteria,root.destination)

# ***** MAIN PROGRAM *****

# create window
root = tk.Tk()
root.geometry("800x600")
root.title("File Renamer")

# *** create entry screen ***
# zipped file picker
tk.Label(root, text="Zipped file location").grid(row=1, column=0)
zip_btn = tk.Button(root, text="Choose File", command=zip_btn_click)
zip_btn.grid(row=1,column=1)

# desitnation folder
tk.Label(root, text="Destination folder").grid(row=2, column=0)
dest_btn = tk.Button(root, text="Choose Folder", command=dest_btn_click)
dest_btn.grid(row=2,column=1)

# criteria sheet
tk.Label(root, text="Criteria Sheet").grid(row=3, column=0)
crit_btn = tk.Button(root, text="Choose File", command=crit_btn_click)
crit_btn.grid(row=3,column=1)

# go button
go_btn = tk.Button(root, text="Go", command=go_btn_click)
go_btn.grid(row=4,column=1)

# global variables
root.zipped_file = '11.FIA1___Creating_with_Code___Investigation_Final.zip'
root.destination = 'student_files'
root.criteria = 'criteria.pdf'

# run window loop
root.mainloop()