from zipfile import ZipFile
import os
import shutil

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
            


# ----- MAIN PROGRAM -----
zipped_file = '11.FIA1___Creating_with_Code___Investigation_Final.zip'
destination = 'student_files'
criteria = 'criteria.pdf'

unzip(zipped_file, destination)
rename_files(destination)
add_file(criteria,destination)