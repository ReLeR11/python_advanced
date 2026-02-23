class InvalidColumnError(Exception):
    pass


class FullColumnError(Exception):
    pass


def create_matrix(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]


def print_matrix(ma):
    for line in ma:
        print(line)


def validate_column_choice(column, max_idx):
    if not (0 <= column < max_idx):
        raise InvalidColumnError


def place_player_choice(ma, c, player_n):
    for r in range(len(ma) - 1, -1, -1):
        if ma[r][c] == 0:
            ma[r][c] = player_n
            return r, c
    raise FullColumnError


def is_player_num(ma, r, c, player_n):
    try:
        return ma[r][c] == player_n
    except IndexError:
        return False


def is_vertical_win(ma, r, c, player_n, slots):
    return all(is_player_num(ma, r + idx, c, player_n) for idx in range(slots))


def is_horizontal_win(ma, r, c, player_n, slots):
    filled = 1

    for idx in range(1, slots):
        if is_player_num(ma, r, c + idx, player_n):
            filled += 1
        else:
            break

    for idx in range(1, slots):
        if is_player_num(ma, r, c - idx, player_n):
            filled += 1
        else:
            break

    return filled >= slots


def is_left_diagonal_win(ma, r, c, player_n, slots):
    filled = 1

    for idx in range(1, slots):
        if is_player_num(ma, r + idx, c + idx, player_n):
            filled += 1
        else:
            break

    for idx in range(1, slots):
        if is_player_num(ma, r - idx, c - idx, player_n):
            filled += 1
        else:
            break

    return filled >= slots


def is_right_diagonal_win(ma, r, c, player_n, slots):
    filled = 1

    for idx in range(1, slots):
        if is_player_num(ma, r - idx, c + idx, player_n):
            filled += 1
        else:
            break

    for idx in range(1, slots):
        if is_player_num(ma, r + idx, c - idx, player_n):
            filled += 1
        else:
            break

    return filled >= slots


def is_winner(ma, r, c, player_n, slots):
    return (
            is_vertical_win(ma, r, c, player_n, slots) or
            is_horizontal_win(ma, r, c, player_n, slots) or
            is_left_diagonal_win(ma, r, c, player_n, slots) or
            is_right_diagonal_win(ma, r, c, player_n, slots)
    )


SLOTS = 4
row_count = 6
cols_count = 7

matrix = create_matrix(row_count, cols_count)

print_matrix(matrix)

player_num = 1
counter = 0

while True:
    try:
        column_num = int(input(f"Player {player_num}, please choose a column: ")) - 1
        validate_column_choice(column_num, cols_count)
        row, col = place_player_choice(matrix, column_num, player_num)
        print_matrix(matrix)
    except ValueError:
        print("This is not a number! Please, select a valid number!")
        continue
    except InvalidColumnError:
        print(f"Please select a number between 1 and {cols_count}")
        continue
    except FullColumnError:
        print("This column is full! Please, select another!")
        continue

    if is_winner(matrix, row, col, player_num, SLOTS):
        print(f"The winner is Player {player_num}!")
        break

    counter += 1
    if row_count * cols_count == counter:
        print("The game is draw!")
        break

    player_num = 2 if player_num == 1 else 1