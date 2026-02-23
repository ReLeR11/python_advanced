def boarding_passengers(*args):
    capacity = args[0]
    boarded = {}
    guests_waiting = False

    for passengers, program in args[1:]:
        if passengers <= capacity:
            if program not in boarded:
                boarded[program] = 0
            boarded[program] += passengers
            capacity -= passengers

        else:
            guests_waiting = True
            if capacity <= 0:
                break


    sorted_boarded = sorted(boarded.items(), key=lambda kvp: (-kvp[1], kvp[0]))

    boarding_details = ["Boarding details by benefit plan:"]
    for program, passengers in sorted_boarded:
        boarding_details.append(f"## {program}: {passengers} guests")
    if not guests_waiting:
        boarding_details.append("All passengers are successfully boarded!")
    elif capacity <= 0:
        boarding_details.append("Boarding unsuccessful. Cruise ship at full capacity.")
    else:boarding_details.append(f"Partial boarding completed. Available capacity: {capacity}.")

    return "\n".join(boarding_details)
