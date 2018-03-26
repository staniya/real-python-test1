import os
import glob

my_path = r"/Users/staniya/Downloads/book1-exercises-master/chp09/practice_files/little pics"
files_of_jpg = os.path.join(my_path, "*/*.jpg")

for files in glob.glob(files_of_jpg):
    size_of_files = os.path.getsize(files)
    if size_of_files < 2000:
        print(f"Currently removing {files}")
        delete_files = os.remove(files)
        check = os.path.exists(files)

import os

my_path = r"/Users/staniya/Downloads/book1-exercises-master/chp09/practice_files/little pics"

for current_folder, subfolders, file_names in os.walk(my_path):
    for file_name in file_names:
        full_path = os.path.join(current_folder, file_name)
        check_jpg = file_name.lower().endswith(".jpg")
        check_size = os.path.getsize(file_name)
        if check_jpg and check_size:
            print(f"Currently removing {files}")
            os.remove(full_path)
