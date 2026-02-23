number_of_commands = int(input())
parking = set()

for command in range(number_of_commands):
    direction, car_number = input().split(", ")

    if direction == "IN":
        parking.add(car_number)

    elif car_number in parking:
        parking.remove(car_number)

if not parking:
    print("Parking Lot is Empty")

else:
    for car in parking:
        print(car)
