from d2p1 import unlock_toilet
from intrepid_calendar import read_input_data


def test_case_one():
    assert unlock_toilet("ULL\nRRDDD\nLURDL\nUUUUD") == "1985"


def test_custom_case_one():
    assert unlock_toilet("U") == '2'


def test_custom_case_two():
    assert unlock_toilet("D") == '8'


def test_custom_case_three():
    assert unlock_toilet("L") == '4'


def test_custom_case_four():
    assert unlock_toilet("R") == '6'


# Edge cases

def test_custom_case_five():
    assert unlock_toilet("ULL") == '1'


def test_custom_case_six():
    assert unlock_toilet("URR") == '3'


def test_custom_case_seven():
    assert unlock_toilet("ULU") == '1'


def test_custom_case_eight():
    assert unlock_toilet("URU") == '3'


def test_custom_case_nine():
    assert unlock_toilet("DLD") == '7'


def test_custom_case_ten():
    assert unlock_toilet("DRD") == '9'


def test_custom_case_eleven():
    assert unlock_toilet("DLL") == '7'


def test_custom_case_twelve():
    assert unlock_toilet("DRR") == '9'


def test_custom_case_thirteen():
    assert unlock_toilet("UU") == '2'


def test_custom_case_fourteen():
    assert unlock_toilet("DD") == '8'


def test_custom_case_fifteen():
    assert unlock_toilet("LL") == '4'


def test_custom_case_sixteen():
    assert unlock_toilet("RR") == '6'


def test_answer():
    assert unlock_toilet(read_input_data(2)) == "56983"
