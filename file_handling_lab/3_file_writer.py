import os.path

from constants import path_to_dir

path = os.path.join(path_to_dir, "python_advanced", "my_files", "my_first_file.txt")

with open("my_first_file.txt", "w") as file:
    file.write("I just created my first file!")
