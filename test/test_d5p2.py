import d5p2
from intrepid_calendar import read_input_data


def test_one():
    assert d5p2.is_interesting("abc", "3231929") == ("1", "5")


def test_two():
    print(d5p2.is_interesting("abc", "5017308"))
    assert d5p2.is_interesting("abc", "5017308") == ("8", None)


def test_three():
    assert d5p2.is_interesting("abc", "5357525") == ("4", "e")


def test_four():
    print(d5p2.naive_hashthrash_me_a_password("abc"))
    assert d5p2.naive_hashthrash_me_a_password("abc") == "05ace8e3"


def test_answer():
    assert d5p2.naive_hashthrash_me_a_password(read_input_data(5)) == "1050cbbd"
