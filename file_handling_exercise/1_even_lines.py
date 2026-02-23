import os

from constants import path_to_dir

path = os.path.join(path_to_dir, "python_advanced", "file_handling_exercise", "text.txt")

with open("text.txt") as file:
    for line_index, line in enumerate(file):
        if line_index % 2 == 0:
            for ch in "-,.!?":
                line = line.replace(ch, "@")

            print(" ".join(reversed(line.split())))
