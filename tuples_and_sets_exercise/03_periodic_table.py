number_of_lines = int(input())

chemical_elements = set()

for _ in range(number_of_lines):
    element = input().split()
    for el in element:
        chemical_elements.add(el)

print(*chemical_elements, sep="\n")
