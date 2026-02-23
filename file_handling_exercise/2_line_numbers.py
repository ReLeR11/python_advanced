import os

from constants import path_to_dir
from string import punctuation

path = os.path.join(path_to_dir, "python_advanced", "file_handling_exercise", "text.txt")

with open("text.txt") as file, open("output.txt", "w") as output:
    result = []
    for row_index, line in enumerate(file):
        letter_count = 0
        punctuation_count = 0

        for ch in line:
            if ch.isalpha():
                letter_count += 1

            elif ch in punctuation:
                punctuation_count += 1

        result.append(f"Line {row_index + 1}: {line.strip()} ({letter_count})({punctuation_count})")

    output.write("\n".join(result))
