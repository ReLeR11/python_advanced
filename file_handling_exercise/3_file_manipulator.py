import os
print(os.getcwd())

while True:
    line = input()
    if line == "End":
        break

    command, name_file, *args = line.split("-")

    if command == "Create":
        open(name_file, "w").close()

    elif command == "Add":
        with open(name_file, "a") as file:
            file.write(f"{args[0]}\n")

    elif command == "Replace":
        try:
            with open(name_file, "r+") as file:
                content = file.read()
                file.seek(0)
                file.truncate()
                file.write(content.replace(args[0], args[1]))

        except FileNotFoundError:
            print("An error occurred")

    elif command == "Delete":
        if os.path.exists(name_file):
            os.remove(name_file)

        else:
            print("An error occurred")
