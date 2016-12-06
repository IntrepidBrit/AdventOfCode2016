import d5p1
from intrepid_calendar import read_input_data

def test_one():
    assert d5p1.is_interesting("abc", "3231929") == "1"


def test_two():
    assert d5p1.is_interesting("abc", "5017308") == "8"


def test_three():
    assert d5p1.is_interesting("abc", "5278568") == "f"


def test_four():
    assert d5p1.naive_hashthrash_me_a_password("abc") == "18f47a30"


def test_answer():
    assert d5p1.naive_hashthrash_me_a_password(read_input_data(5)) == "4543c154"