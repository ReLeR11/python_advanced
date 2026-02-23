def set_cover(universe, sets):
    universe_sets = set(universe)
    chosen_sets = []
    remaining_sets = sets.copy()

    while universe_sets and remaining_sets:
        best_set = max(remaining_sets, key=lambda s: len(universe_sets.intersection((s))))
        if not universe_sets.intersection(best_set):
            break
        chosen_sets.append(best_set)
        universe_sets -= set(best_set)
        remaining_sets.remove(best_set)

    if universe_sets:
        return  None
    return chosen_sets

universes = list(map(int, input().split(", ")))
n = int(input())
sets = []

for _ in range(n):
    set_elements = list(map(int, input().split(", ")))
    sets.append(set_elements)

result = set_cover(universes, sets)

if result is None:
    print("No solution exist")
else:
    for i in range(len(result)):
        result[i] = sorted(result[i])

    print(f"\nSets to take ({len(result)}): ")

    for s in result:
        print("{", ", ".join(map(str, s)), "}")
