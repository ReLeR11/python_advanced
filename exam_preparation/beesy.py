size_field = int(input())

energy = 15
needed_nectar = 30
energy_restored = False
nectar = 0

bee_row, bee_col = 0, 0
field = []


for row in range(size_field):
    field.append(list(input()))
    for col in range(size_field):
        if field[row][col] == "B":
            bee_row, bee_col = row, col
            field[row][col] = "-"


def bee_moves(direction, cur_row, cur_col):
    if direction == "up":
        cur_row = (cur_row - 1) % size_field

    elif direction == "down":
        cur_row = (cur_row + 1) % size_field

    elif direction == "left":
        cur_col = (cur_col - 1) % size_field

    elif direction == "right":
        cur_col = (cur_col + 1) % size_field

    return cur_row, cur_col


while True:
    energy -= 1
    bee_row, bee_col = bee_moves(input(), bee_row, bee_col)

    if field[bee_row][bee_col].isdigit():
        nectar += int(field[bee_row][bee_col])
        field[bee_row][bee_col] = "-"

    if field[bee_row][bee_col] == "H":
        if nectar >= needed_nectar:
            print(f"Great job, Beesy! The hive is full. Energy left: {energy}")
        else:
            print("Beesy did not manage to collect enough nectar.")
        break

    if energy <= 0:
        if not energy_restored and nectar >= needed_nectar:
            energy += nectar - needed_nectar
            energy_restored = True
            nectar = needed_nectar

        else:
            print("This is the end! Beesy ran out of energy.")
            break

field[bee_row][bee_col] = "B"

for row in field:
    print(''.join(row))
