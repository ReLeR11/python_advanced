numbers = tuple([float(number) for number in input().split()])

count_number = {}

for number in numbers:
    if number not in count_number:
        count_number[number] = numbers.count(number)

for key, value in count_number.items():
    print(f"{key:.1f} - {value} times")
