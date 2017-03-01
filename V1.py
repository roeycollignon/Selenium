# import
from zipfile import *
import os

# set build path
builddir = r'C:\Users\roey.c\Desktop\lab_days'

# for all sub-folders inside the build folder
for subdir, dirs, files in os.walk(builddir):
    print subdir, dirs, files

    # change the current directory
    os.chdir(subdir)

    # for each file in the current folder
    for file in files:
        if is_zipfile(file):
            print "true"
        else:
            print "false"

        if file=="NetworkingPackage.zip":
            file_name = "NetworkingPackage.zip"
            zip_archive = ZipFile(file_name)
            print zip_archive.namelist()
            zip_archive.close()


def zipi():
    file_name = "bla.zip"
    zip_archive = ZipFile(file_name)
    print zip_archive.infolist();
    zip_archive.close()
