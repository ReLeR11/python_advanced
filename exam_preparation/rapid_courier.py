from collections import deque


packages = [int(x) for x in input().split()]
couriers = deque(int(x) for x in input().split())

total_weight = 0

while couriers and packages:
    package = packages[-1]
    courier = couriers.popleft()

    if courier >= package:
        total_weight += package
        packages.pop()
        courier -= package * 2

        if courier > 0:
            couriers.append(courier)

    else:
        packages[-1] -= courier
        total_weight += courier

print(f"Total weight: {total_weight} kg")

if not couriers and not packages:
    print("Congratulations, all packages were delivered successfully by the couriers today.")

elif not couriers and packages:
    print(f"Unfortunately, there are no more available couriers to deliver the following packages: "
          f"{', '.join(str(pac) for pac in packages)}")

else:
    print(f"Couriers are still on duty: {', '.join(str(cur) for cur in couriers)} "
          f"but there are no more packages to deliver.")
