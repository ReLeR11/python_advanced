size_square_matrix = int(input())

matrix = []

for _ in range(size_square_matrix):
    data = [int(x) for x in input().split()]
    matrix.append(data)

diagonal_sum = 0

for row_index in range(size_square_matrix):
    for column_index in range(size_square_matrix):
        if row_index == column_index:
            diagonal_sum += matrix[row_index][column_index]

print(diagonal_sum)
