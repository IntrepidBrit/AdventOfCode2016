class Keypad:
    def __init__(self):
        self.board = "123456789"
        self.board_width = 3
        self.board_height = 3
        self.finger_position = 4

    def is_legal_move(self, pos, instruction):
        new_pos = pos
        if instruction == "U":
            new_pos = pos - self.board_width
        if instruction == "D":
            new_pos = pos + self.board_width
        if instruction == "L":
            new_pos = pos - 1 if (pos - 1) // self.board_width == pos // self.board_width else pos
        if instruction == "R":
            new_pos = pos + 1 if (pos + 1) // self.board_width == pos // self.board_width else pos

        if 0 <= new_pos <= 8:
            return new_pos
        else:
            return pos

    def solve_digit_instuctions(self, instructions):
        for move in instructions:
            # print("pos", self.finger_position, "value", self.board[self.finger_position])
            self.finger_position = self.is_legal_move(self.finger_position, move)

        # print("FINAL pos", self.finger_position, "value", self.board[self.finger_position])
        return self.board[self.finger_position]


def unlock_toilet(obtuse_instructions):
    keypad = Keypad()
    digit_instructions = obtuse_instructions.split('\n')
    return "".join([keypad.solve_digit_instuctions(instruction) for instruction in digit_instructions])
