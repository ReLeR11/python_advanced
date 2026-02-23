size_field = int(input())

matrix = []
bunny = []

for row in range(size_field):
    matrix.append(input().split())
    for col in range(size_field):
        if matrix[row][col] == "B":
            bunny = [row, col]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

max_eggs = float("-inf")
max_direction = ""
max_matrix = []

for direction, move in directions.items():
    eggs = 0
    current_matrix = []
    row = bunny[0] + move[0]
    col = bunny[1] + move[1]

    while 0 <= row < size_field and 0 <= col < size_field:
        if matrix[row][col] == "X":
            break
        eggs += int(matrix[row][col])
        current_matrix.append([row, col])
        row += move[0]
        col += move[1]

    if current_matrix and eggs > max_eggs:
        max_eggs = eggs
        max_direction = direction
        max_matrix = current_matrix

print(max_direction)
[print(row) for row in max_matrix]
print(max_eggs)
