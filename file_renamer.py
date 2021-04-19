from zipfile import ZipFile
import os

def unzip(file,dest):
    try:
        with ZipFile(file, 'r') as zipped:
            zipped.extractall(dest)
    except:
        print("Zip file error")

def rename():
    pass




# ----- MAIN PROGRAM -----
zipped_file = '11.FIA1___Creating_with_Code___Investigation_Final.zip'
destination = 'student_files'

unzip(zipped_file, destination)