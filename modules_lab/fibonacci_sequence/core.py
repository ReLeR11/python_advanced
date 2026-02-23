def fibonacci(n):
    sequence = [0, 1]

    for num in range(n-2):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence


def locate(num, sequence):
    try:
        index = sequence.index(num)
        return f"The number - {num} is at index {index}"


    except ValueError:
        return f"The number {num} is not in the sequence"
