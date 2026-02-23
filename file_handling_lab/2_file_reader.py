import os.path

from constants import path_to_dir

path = os.path.join(path_to_dir, "python_advanced", "my_files", "numbers.txt")

file = open(path)

total = 0

for line in file:
    total += int(line)

print(total)
file.close()
