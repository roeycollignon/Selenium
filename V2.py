# import
from zipfile import *
import os


def extract_zip_file(file_name, dir_path):

    zip_archive = ZipFile(file_name)
    print zip_archive.namelist()

    new_path = dir_path+'\\'+file_name
    new_path = new_path.split(".zip")
    new_path = new_path[0]
    os.makedirs(new_path)
    zip_archive.extractall(new_path)
    zip_archive.close()


def get_requirements():

    # for all sub-folders inside the build folder
    for subdir, dirs, files in os.walk(builddir):
        print subdir, dirs, files

        # change the current directory
        os.chdir(subdir)

        # for each file in the current folder
        for file in files:
            if is_zipfile(file):
                extract_zip_file(file, subdir)

# This is the main
# set build path
builddir = r'C:\Users\idan\Desktop\lab_days1'
get_requirements()
