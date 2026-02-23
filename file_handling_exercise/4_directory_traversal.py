import os


files = {}
directory = "../"

def directory_traversal(folder, level=1):
    if level == -1:
        return
    for element in os.listdir(folder):
        f = os.path.join(folder, element)
        if os.path.isfile(f):
            ext = os.path.splitext(element)[1]
            if ext not in files:
                files[ext] = []
            files[ext].append(element)

        else:
            directory_traversal(f, level - 1)

directory_traversal(directory)

with open(os.path.join(directory, "report.txt"), "w") as output_file:
    for extension, file_names in sorted(files.items()):
        output_file.write(f"{extension}\n")
        for file_name in sorted(file_names):
            output_file.write(f"- - - {file_name}\n")
