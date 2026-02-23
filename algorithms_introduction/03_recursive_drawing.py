def print_figure(num):
    if num <= 0:
        return

    print("*" * num)

    print_figure(num - 1)

    print("#" * num)

number = int(input())
print_figure(number)
