from collections import deque

colors_string = deque(input().split())

main_colors = ["red", "yellow", "blue"]
secondary_colors = {
    "orange": ["red", "yellow"],
    "purple": ["red", "blue"],
    "green": ["yellow", "blue"]
}

colors = []

while colors_string:
    first_string = colors_string.popleft()
    last_string = colors_string.pop() if colors_string else ""

    for color in (first_string + last_string, last_string + first_string):
        if color in main_colors or color in secondary_colors:
            colors.append(color)
            break

    else:
        if len(first_string) > 1:
            colors_string.insert(len(colors_string) // 2, first_string[:-1])
        if len(last_string) > 1:
            colors_string.insert(len(colors_string) // 2, last_string[:-1])

for color in colors:
    if color in secondary_colors:
        for el in secondary_colors[color]:
            if el not in colors:
                colors.remove(color)
                break

print(colors)
