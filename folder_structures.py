import os
import glob

#my_input_file = open("C:/Documents/Learning Python/hello.txt", "r")

my_path = "/Users/staniya/Downloads/book1-exercises-master/chp09/practice_files"
input_file_name = os.path.join(my_path, "example.txt")

with open(input_file_name, "r") as my_input_file:
    for line in my_input_file.readlines():
        print(line)


my_path = "/Users/staniya/Downloads/book1-exercises-master/chp09/practice_files/images"

#get a list of all files and folders
file_names_list = os.listdir(my_path)

#loop over every file in the main folder
for file_name in file_names_list:
    if file_name.lower().endswith(".gif"): #extention matches a GIF file
        print(f"Converting {file_name} to JPG")
        #get full path name and change the ".gif" to ".jpg"
        full_file_name = os.path.join(my_path, file_name)
        new_file_name = full_file_name[0:(len(full_file_name) - 4)] + ".jpg"
        os.rename(full_file_name, new_file_name)

        
        
my_path = "/Users/staniya/Downloads/book1-exercises-master/chp09/practice_files/images"
possible_files = os.path.join(my_path, "*.gif")

for file_name in glob.glob(possible_files):
    print(f"Converting {file_name} to JPG")
    full_file_name = os.path.join(my_path, file_name)
    new_file_name = full_file_name[0:len(full_file_name)-4] + ".jpg"
    os.rename(full_file_name, new_file_name)


my_path = "/Users/staniya/Downloads/book1-exercises-master/chp09/practice_files/images"
possible_files = os.path.join(my_path, "*/*.png")

for file_name in glob.glob(possible_files):
    print(file_name)


files_and_folders = os.listdir(my_path)

for folder_name in files_and_folders:
    full_path = os.path.join(my_path, folder_name)
    if os.path.isdir(full_path):
        os.rename(full_path, full_path + "folder")


my_path = "/Users/staniya/Downloads/book1-exercises-master/chp09/practice_files/images"

for current_folder, subfolders, file_names in os.walk(my_path):
    for file_name in file_names:
        print(os.path.join(current_folder, file_name))

import os

my_path = "/Users/staniya/Downloads/book1-exercises-master/chp09/practice_files/images"
file_names_list = os.listdir(my_path)

for file_name in file_names_list:
    full_path = os.path.join(my_path, file_name)
    print(full_path)

import os
import glob

my_path = "/Users/staniya/Downloads/book1-exercises-master/chp09/practice_files/images"

for current_folder, subfolders, file_names in os.walk(my_path):
    file_names_list = os.path.join(my_path, "*.png")
    for file_name in glob.glob(file_names_list):
        print(f"Converting {file_name} tp JPG")
        full_file_name = os.path.join(my_path, file_name)
        new_file_name = full_file_name[0: len(full_file_name)-4] + ".jpg"
        os.rename(full_file_name, new_file_name)
        print(new_file_name)

file_names_list = os.path.join(my_path, "*.jpg")
for file in glob.glob(file_names_list):
    jpg_exists = os.path.exists(file)
    print(file)
