import os

from constants import path_to_dir

path = os.path.join(path_to_dir, "python_advanced", "file_handling_lab", "my_first_file.txt")

if os.path.exists(path):
    os.remove(path)

else:
    print("File already deleted!")
