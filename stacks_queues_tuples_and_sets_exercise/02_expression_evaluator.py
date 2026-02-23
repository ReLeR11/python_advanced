from collections import deque

string_expression = input().split()

numbers = deque()

operators = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x // y
}

for symbol in string_expression:
    if symbol not in "+-*/":
        numbers.append(int(symbol))

    else:
        while len(numbers) > 1:
            first_number = numbers.popleft()
            second_number = numbers.popleft()
            result = operators[symbol](first_number, second_number)
            numbers.appendleft(result)

print(numbers[0])
