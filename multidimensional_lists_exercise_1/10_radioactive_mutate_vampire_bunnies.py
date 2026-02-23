rows, cols = [int(x) for x in input().split()]

matrix = []
player_row, player_col = 0, 0
bunnies = set()

for row in range(rows):
    matrix.append(list(input()))
    for col in range(cols):
        if matrix[row][col] == "P":
            player_row, player_col = row, col
        elif matrix[row][col] == "B":
            bunnies.add((row, col))

commands = list(input())
player_won = False

moves = {
    "U": lambda r, c: (r - 1, c),
    "D": lambda r, c: (r + 1, c),
    "L": lambda r, c: (r, c - 1),
    "R": lambda r, c: (r, c + 1)
}


def spread_bunnies(mat, bunnies_set):
    new_bunnies = set()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for b_row, b_col in bunnies_set:
        for d_row, d_col in directions:
            new_rol, new_col = b_row + d_row, b_col + d_col
            if 0 <= new_rol < len(mat) and 0 <= new_col < len(mat[0]):
                mat[new_rol][new_col] = "B"
                new_bunnies.add((new_rol, new_col))

    return mat, bunnies_set.union(new_bunnies)


for command in commands:
    new_p_row, new_p_col = moves[command](player_row, player_col)
    matrix, bunnies = spread_bunnies(matrix, bunnies)

    if (player_row, player_col) not in bunnies:
        matrix[player_row][player_col] = "."

    if new_p_row < 0 or new_p_row >= rows or new_p_col < 0 or new_p_col >= cols:
        player_won = True
        break

    player_row, player_col = new_p_row, new_p_col
    if matrix[player_row][player_col] == "B":
        break

for row in matrix:
    print("".join(row))

if player_won:
    print(f"won: {player_row} {player_col}")
else:
    print(f"dead: {player_row} {player_col}")
