orientation_matrix = [[0, 1],
                      [1, 0],
                      [0, -1],
                      [-1, 0]]


def handle_instruction(position, orientation, instruction, block_history):
    revisited_block = None
    direction = instruction[0]
    distance = int(instruction[1:])

    orientation += 1 if direction == "R" else -1

    new_orientation = orientation_matrix[orientation % len(orientation_matrix)]
    x = y = None
    for d in range(1, distance + 1):
        x = position[0] + new_orientation[0]*d
        y = position[1] + new_orientation[1]*d
        try:
            if y in block_history[x]:
                revisited_block = [x,y]
            else:
                block_history[x][y] = True
        except KeyError:
                block_history[x] = {y: True}

    position[0] = x
    position[1] = y
    return position, orientation, revisited_block


def detect_double_visit(directions_string):
    instructions = directions_string.split(",")

    my_position = [0, 0]
    my_orientation = 0

    block_history = {}
    revisited_block = None

    for instruction in instructions:
        if revisited_block is None:
            my_position, my_orientation, revisited_block = handle_instruction(my_position, my_orientation, instruction.strip(), block_history)

    return revisited_block[0] + revisited_block[1]


