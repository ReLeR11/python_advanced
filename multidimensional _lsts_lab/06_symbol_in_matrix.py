size_square_matrix = int(input())

matrix = []

for _ in range(size_square_matrix):
    data = list(input())
    matrix.append(data)

searched_symbol = input()
position = None
is_found = False

for row_index in range(size_square_matrix):
    for column_index in range(size_square_matrix):
        if matrix[row_index][column_index] == searched_symbol:
            position = (row_index, column_index)
            is_found = True
            break
    if is_found:
        break

if position:
    print(position)
else:
    print(f"{searched_symbol} does not occur in the matrix")
