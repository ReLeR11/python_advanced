def if_chek_row_winner(cur_board, sign):
    for cur_row in cur_board:
        if cur_row.count(sign) == 3:
            return True

    return False


def if_check_column_winner(cur_board, sign):
    for col_index in range(size_of_board):
        count = 0
        for row_index in range(size_of_board):
            if cur_board[row_index][col_index] == sign:
                count += 1

        if count == 3:
            return True

    return False


def if_check_diagonal_winner(cur_board, sign):
    count_primary = 0
    count_secondary = 0
    for index in range(size_of_board):
        if cur_board[index][index] == sign:
            count_primary += 1

        if cur_board[index][size_of_board - 1 - index] == sign:
            count_secondary += 1

    if count_primary == 3 or count_secondary == 3:
        return True

    return False


def if_check_for_winner(cur_board, sign):
    if (if_chek_row_winner(cur_board, sign)
            or if_check_column_winner(cur_board, sign)
            or if_check_diagonal_winner(cur_board, sign)):
        return True

    return False


def print_board(cur_board):
    for cur_row in cur_board:
        print(f" | {' |  '.join(cur_row)} |")


player_1_name = input("Player one name: ")
player_2_name = input("Player two name: ")
player_1_sign = input(f"{player_1_name} would you like to play with 'X' or 'O'? : ").upper()

while player_1_sign != "X" and player_1_sign != "O":
    print("Please enter either 'X' or 'O'.")
    player_1_sign = input(f"{player_1_name} would you like to play with 'X' or 'O'? : ").upper()

player_2_sign = "O" if player_1_sign == "X" else "X"

print("This is numeration of the board:")
print("| 1 | 2 | 3 |")
print("| 4 | 5 | 6 |")
print("| 7 | 8 | 9 |")

print(f"{player_1_name} starts first!")

turn = 1
size_of_board = 3
board = [[" ", " ", " "] for _ in range(size_of_board)]
mapper = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2)
}

winner = False

while turn < 10:
    current_player = player_1_name if turn % 2 != 0 else player_2_name
    current_sign = player_1_sign if turn % 2 != 0 else player_2_sign

    try:
        position = int(input(f"{current_player} please choose a free position between [1-9]: "))

    except ValueError:
        print("Please enter a valid number.")
        continue

    if not (1 <= position <= 9):
        print("Please enter a valid number, between 1 and 9.")
        continue

    row, column = mapper[position]
    if board[row][column] != " ":
        print("This position is already occupied.")
        continue

    board[row][column] = current_sign
    print_board(board)

    if turn >= 5 and if_check_for_winner(board, current_sign):
        print(f"Congratulation! {current_player} wins!")
        winner = True
        break

    turn += 1

if not winner:
    print("Thanks for playing, no winner today!")
    print_board(board)
