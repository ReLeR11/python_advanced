matrix_rows = int(input())

numbers = []

for _ in range(matrix_rows):
    data = [int(x) for x in input().split(", ")]
    numbers.extend(data)
print(numbers)
