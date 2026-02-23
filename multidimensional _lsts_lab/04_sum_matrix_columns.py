n_rows, n_columns = [int(x) for x in input().split(", ")]

matrix = []

for _ in range(n_rows):
    data = [int(x) for x in input().split()]
    matrix.append(data)

for col_index in range(n_columns):
    columns_sum = 0
    for row_index in range(n_rows):
        columns_sum += matrix[row_index][col_index]
    print(columns_sum)
