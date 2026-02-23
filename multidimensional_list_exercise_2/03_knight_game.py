board_dimensions = int(input())

matrix = []
knights = []

for row in range(board_dimensions):
    matrix.append([x for x in input()])
    for col in range(board_dimensions):
        if matrix[row][col] == "K":
            knights.append([row, col])

removed_knights = 0
possible_moves = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]

while True:
    max_hits = 0
    max_knight = [0, 0]

    for k_row, k_col in knights:
        hits = 0

        for move in possible_moves:
            target_row = k_row + move[0]
            target_col = k_col + move[1]

            if 0 <= target_row < board_dimensions and 0 <= target_col < board_dimensions:
                if matrix[target_row][target_col] == "K":
                    hits += 1

        if hits > max_hits:
            max_hits = hits
            max_knight = [k_row, k_col]

    if max_hits == 0:
        break

    knights.remove(max_knight)
    matrix[max_knight[0]][max_knight[1]] = "0"
    removed_knights += 1

print(removed_knights)
