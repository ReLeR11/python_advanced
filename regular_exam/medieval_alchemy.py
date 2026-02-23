from collections import deque


substances = [int(subs) for subs in input().split(", ")]
crystals = deque(int(cry) for cry in input().split(", "))

potions_to_craft = {
    110: "Brew of Immortality",
    100: "Essence of Resilience",
    90: "Draught of Wisdom",
    80: "Potion of Agility",
    70: "Elixir of Strength"
}

crafted = []
crafted_set = set()

while substances and crystals:
    substance = substances.pop()
    crystal = crystals.popleft()
    energy = substance + crystal

    if energy in potions_to_craft and potions_to_craft[energy] not in crafted_set:
        potion_name = potions_to_craft[energy]
        crafted.append(potion_name)
        crafted_set.add(potion_name)

    else:
        possible = [req for req, name in potions_to_craft.items() if req <= energy and name not in crafted_set]

        if possible:
            best_req = max(possible)
            potion_name = potions_to_craft[best_req]
            crafted.append(potion_name)
            crafted_set.add(potion_name)

            new_crystal = crystal - 20
            if new_crystal > 0:
                crystals.append(new_crystal)

        else:
            new_crystal = crystal - 5
            if new_crystal > 0:
                crystals.append(new_crystal)

    if len(crafted_set) == 5:
        break



success = len(crafted_set) == 5
if success:
    print("Success! The alchemist has forged all potions!")

else:
    print("The alchemist failed to complete his quest.")

if crafted:
    print(f"Crafted potions: {', '.join(crafted)}")

if substances:
    print(f"Substances: {', '.join(map(str, reversed(substances)))}")

if crystals:
    print(f"Crystals: {', '.join(map(str, crystals))}")
