number_of_names = int(input())

odd_set = set()
even_set = set()

for row in range(1, number_of_names + 1):
    value_name = sum(ord(ch) for ch in input()) // row

    if value_name % 2 == 0:
        even_set.add(value_name)

    else:
        odd_set.add(value_name)

if sum(odd_set) == sum(even_set):
    result = even_set | odd_set

elif sum(odd_set) > sum(even_set):
    result = odd_set - even_set

else:
    result = even_set ^ odd_set

print(*result, sep=", ")
