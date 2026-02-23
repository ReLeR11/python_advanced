from python_advanced.modules_lab.fibonacci_sequence.core import fibonacci, locate

command = input()
sequence = None

while command != "Stop":
    num = int(command.split()[-1])

    if command.startswith("Create"):
        sequence = fibonacci(num)
        print(*sequence)

    else:
        if sequence:
            print(locate(num, sequence))

        else:
            print("Please first  initialize a sequence.")

    command = input()
