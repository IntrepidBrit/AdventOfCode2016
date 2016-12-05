class Button:
    up = down = left = right = None

    def __init__(self, value):
        self.value = value

    def configure_neighbours(self, up=None, down=None, left=None, right=None, referred=False):

        if up is not None:
            self.up = up
            if referred is False:
                up.configure_neighbours(down=self, referred=True)

        if down is not None:
            self.down = down
            if referred is False:
                down.configure_neighbours(up=self, referred=True)

        if left is not None:
            self.left = left
            if referred is False:
                left.configure_neighbours(right=self, referred=True)

        if right is not None:
            self.right = right
            if referred is False:
                right.configure_neighbours(left=self, referred=True)

    def move(self, direction):
        new_pos = None
        if direction == "U":
            new_pos = self.up
        elif direction == "D":
            new_pos = self.down
        elif direction == "L":
            new_pos = self.left
        elif direction == "R":
            new_pos = self.right
        return self if new_pos is None else new_pos


class Keypad:
    def __init__(self):
        self.pad = [Button("{:X}".format(x)) for x in range(1, 14)]

        self.pad[0].configure_neighbours(down=self.pad[2])
        self.pad[1].configure_neighbours(right=self.pad[2], down=self.pad[5])
        self.pad[2].configure_neighbours(right=self.pad[3], down=self.pad[6])
        self.pad[3].configure_neighbours(down=self.pad[7])
        self.pad[4].configure_neighbours(right=self.pad[5])
        self.pad[5].configure_neighbours(right=self.pad[6], down=self.pad[9])
        self.pad[6].configure_neighbours(right=self.pad[7], down=self.pad[10])
        self.pad[7].configure_neighbours(right=self.pad[8], down=self.pad[11])
        self.pad[9].configure_neighbours(right=self.pad[10])
        self.pad[10].configure_neighbours(down=self.pad[12], right=self.pad[11])

        self.finger_position = self.pad[4]

    def solve_digit_instuctions(self, instructions):
        for instruction in instructions:
            self.finger_position = self.finger_position.move(instruction)

        return self.finger_position.value


def unlock_toilet(obtuse_instructions):
    keypad = Keypad()
    digit_instructions = obtuse_instructions.split('\n')
    return "".join([keypad.solve_digit_instuctions(instruction) for instruction in digit_instructions])
