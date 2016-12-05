import d3p1

from intrepid_calendar import read_input_data

def test_case_one():
    assert not d3p1.is_possible_triangle("10  5  25")


def test_custom_case_one():
    assert d3p1.is_possible_triangle("1  1  1")


def test_custom_case_two():
    assert not d3p1.is_possible_triangle("1  2  3")


def test_custom_case_three():
    assert d3p1.is_possible_triangle("5  7  5")


def test_custom_case_four():
    assert not d3p1.is_possible_triangle("100  100  200")


def test_answer():
    assert d3p1.count_possible_triangles(read_input_data(3)) == 982
