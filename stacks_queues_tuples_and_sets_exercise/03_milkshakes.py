from collections import deque

chocolates = [int(x) for x in input().split(", ")]
cups_of_milk = deque(int(x) for x in input().split(", "))

milkshake = 0

while chocolates and cups_of_milk and milkshake < 5:

    if chocolates[-1] <= 0 and cups_of_milk[0] <= 0:
        chocolates.pop()
        cups_of_milk.popleft()
        continue

    if chocolates[-1] <= 0:
        chocolates.pop()
        continue

    if cups_of_milk[0] <= 0:
        cups_of_milk.popleft()
        continue

    if chocolates[-1] == cups_of_milk[0]:
        milkshake += 1
        chocolates.pop()
        cups_of_milk.popleft()

    else:
        cups_of_milk.rotate(-1)
        chocolates[-1] -= 5

if milkshake == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join(str(x) for x in chocolates)}")
else:
    print("Chocolate: empty")

if cups_of_milk:
    print(f"Milk: {', '.join(str(x) for x in cups_of_milk)}")
else:
    print("Milk: empty")
