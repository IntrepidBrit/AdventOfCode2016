orientations = "NESW"


def navigate(directions_string):
    instructions = directions_string.split(",")

    my_position = {"N": 0, "E": 0, "S": 0, "W": 0}
    my_orientation = 0

    for instruction in instructions:
        direction = instruction.strip()[0]
        distance = instruction.strip()[1:]

        my_orientation += 1 if direction == "R" else -1
        my_position[orientations[my_orientation % len(orientations)]] += int(distance)

    ns = abs(my_position["N"] - my_position["S"])
    ew = abs(my_position["E"] - my_position["W"])

    return ns + ew
