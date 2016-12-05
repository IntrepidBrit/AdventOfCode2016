import os
from d1p1 import navigate
from d1p2 import detect_double_visit
import d2p1
import d2p2
import d3p1
import d3p2


def read_input_data(day_num):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "d{0}.raw".format(day_num)), 'r') as f:
        # Waiting for the moment they try to fill my ram with data. Oh how their mocking laughter will sting my ears.
        data = f.read()

    return data


if __name__ == "__main__":
    print("PREPARE THE CHUNDERDOME!")

    d1_input = read_input_data(1)
    print("Day 1, part 1: ", navigate(d1_input))
    print("Day 1, part 2: ", detect_double_visit(d1_input))

    d2_input = read_input_data(2)
    print("Day 2, part 1: ", d2p1.unlock_toilet(d2_input))
    print("Day 2, part 2: ", d2p2.unlock_toilet(d2_input))

    d3_input = read_input_data(3)
    print("Day 3, part 1: ", d3p1.count_possible_triangles(d3_input))
    print("Day 3, part 2: ", d3p2.count_possible_triangles(d3_input))
