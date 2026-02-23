from collections import deque

bees = deque(int(x) for x in input().split())
nectar = [int(x) for x in input().split()]
operators = deque(input().split())

honey = 0

make_honey = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y if y != 0 else 0
}

while bees and nectar:
    if nectar[-1] >= bees[0]:
        honey += abs(make_honey[operators[0]](bees[0], nectar[-1]))
        bees.popleft()
        nectar.pop()
        operators.popleft()

    else:
        nectar.pop()

print(f"Total honey made: {honey}")
if bees:
    print(f"Bees left: {', '.join(str(x) for x in bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")
