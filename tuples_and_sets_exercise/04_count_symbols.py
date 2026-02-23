text = input()

characters = set()

for ch in text:
    characters.add(ch)

for ch in sorted(characters):
    print(f"{ch}: {text.count(ch)} time/s")
