text = input().split("|")

matrix = []

for i in range(len(text) - 1, -1, -1):
    row = text[i].split()
    if row:
        matrix.append(row)

[print(*row, end=" ") for row in matrix]
