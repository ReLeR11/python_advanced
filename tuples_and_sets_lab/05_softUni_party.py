number_of_guests = int(input())
reservations = set()

for _ in range(number_of_guests):
    reservation = input()
    reservations.add(reservation)

reservation = input()

while reservation != "END":
    if reservation in reservations:
        reservations.remove(reservation)
        reservation = input()

print(len(reservations))
sorted_reservations = sorted(reservations)

for reservation in sorted_reservations:
    print(reservation)
