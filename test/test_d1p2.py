from d1p2 import detect_double_visit
from intrepid_calendar import read_input_data


def test_case_one():
    assert detect_double_visit("R8, R4, R4, R8") == 4


def test_answer():
    assert detect_double_visit(read_input_data(1)) == 126
