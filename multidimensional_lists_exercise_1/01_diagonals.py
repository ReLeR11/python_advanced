square_matrix = int(input())

matrix = [[int(x) for x in input().split(", ")] for _ in range(square_matrix)]

primary_diagonal = [matrix[index][index] for index in range(square_matrix)]
secondary_diagonal = [matrix[index][-1 - index] for index in range(square_matrix)]

print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")
