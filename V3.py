# import
from zipfile import *
import os


def extract_zip_file(file_name, dir_path):

    zip_archive = ZipFile(dir_path+"\\"+file_name)

    new_path = dir_path+'\\'+file_name
    new_path = new_path.split(".zip")
    new_path = new_path[0]
    os.makedirs(new_path)
    zip_archive.extractall(new_path)
    zip_archive.close()

    return new_path

def get_requirements(path):

    dir_content_list = os.listdir(path)

    requirements_list= []
    required_file = "requirements.txt"

    # for each file in the current folder
    for entity in dir_content_list:
        if entity.endswith(".zip"):
            zip_path = extract_zip_file(entity, path)
            returned_value = get_requirements(zip_path)
            if len(returned_value) != 0:
                requirements_list += returned_value
        if entity == required_file:
            file_obj = open((path+"\\"+required_file), 'r')
            requirement_obj = {
                "zip_name": path,
                "file_content": file_obj.read()
            }
            file_obj.close()
            requirements_list.append(requirement_obj)
        if os.path.isdir(path+"\\"+entity):
            returned_value = get_requirements(path+"\\"+entity)
            if len(returned_value) != 0:
                requirements_list += returned_value

    return requirements_list


# This is the main
# set build path
builddir = r'C:\Users\idan\Desktop\l'
print get_requirements(builddir)
