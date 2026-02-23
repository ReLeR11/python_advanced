rows, columns = [int(x) for x in input().split(", ")]

matrix = []

for _ in range(rows):
    data = [int(x) for x in input().split(", ")]
    matrix.append(data)

max_sum_element = float("-inf")
sub_matrix = []

for row_index in range(rows-1):
    for column_index in range(columns-1):
        current_element = matrix[row_index][column_index]
        next_element = matrix[row_index][column_index + 1]
        below_element = matrix[row_index + 1][column_index]
        diagonal_element = matrix[row_index + 1][column_index + 1]

        sum_elements = current_element + next_element + below_element + diagonal_element
        if sum_elements > max_sum_element:
            max_sum_element = sum_elements
            sub_matrix = [[current_element, next_element], [below_element, diagonal_element]]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum_element)
