number_of_names = int(input())
names = set()

for name in range(number_of_names):
    current_name = input()
    names.add(current_name)

for name in names:
    print(name)
