game_field = int(input())

health = 100
immune = False
pacman_row, pacman_column = 0, 0

matrix = []

for row in range(game_field):
    matrix.append(list(input()))
    for column in range(game_field):
        if matrix[row][column] == "P":
            pacman_row, pacman_column = row, column
            matrix[row][column] = "-"

stars = sum(row.count("*") for row in matrix)


def move_pacman(direction, cur_row, cur_col):
    if direction == "up":
        cur_row = (cur_row - 1) % game_field

    if direction == "down":
        cur_row = (cur_row + 1) % game_field

    if direction == "left":
        cur_col = (cur_col - 1) % game_field

    if direction == "right":
        cur_col = (cur_col + 1) % game_field

    return cur_row, cur_col



first_move = True
if first_move:
    matrix[pacman_row][pacman_column] = "-"
    first_move = False


while True:
    command = input()

    if command == "end":
        break

    if first_move:
        matrix[pacman_row][pacman_column] = "-"
        first_move = False

    pacman_row, pacman_column = move_pacman(command, pacman_row, pacman_column)
    if matrix[pacman_row][pacman_column] == "*":
        stars -= 1
        matrix[pacman_row][pacman_column] = "-"
        if stars == 0:
            break

    elif matrix[pacman_row][pacman_column] == "G":
        if immune:
            immune = False
        else:
            health -= 50

        matrix[pacman_row][pacman_column] = "-"

        if health <= 0:
            health = 0
            break

    elif matrix[pacman_row][pacman_column] == "F":
        immune = True
        matrix[pacman_row][pacman_column] = "-"


matrix[pacman_row][pacman_column] = "P"

if health == 0:
    print(f"Game over! Pacman last coordinates [{pacman_row},{pacman_column}]")

elif stars == 0:
    print("Pacman wins! All the stars are collected.")

else:
    print("Pacman failed to collect all the stars.")

print(f"Health: {health}")

if stars > 0:
    print(f"Uncollected stars: {stars}")

for row in matrix:
    print("".join(row))
