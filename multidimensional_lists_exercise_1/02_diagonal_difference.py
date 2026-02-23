square_matrix = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(square_matrix)]

primary_diagonal = [matrix[index][index] for index in range(square_matrix)]
secondary_diagonal = [matrix[index][-1 - index] for index in range(square_matrix)]

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))
