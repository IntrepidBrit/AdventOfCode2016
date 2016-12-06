import d4p1
from intrepid_calendar import read_input_data

tc1 = "aaaaa-bbb-z-y-x-123[abxyz]"
tc2 = "a-b-c-d-e-f-g-h-987[abcde]"
tc3 = "not-a-real-room-404[oarel]"
tc4 = "totally-real-room-200[decoy]"

def test_case_one():
    assert d4p1.room_validator(tc1) == 123


def test_case_two():
    assert d4p1.room_validator(tc2) == 987


def test_case_three():
    assert d4p1.room_validator(tc3) == 404


def test_case_four():
    assert d4p1.room_validator(tc4) == 0


def test_case_five():
    assert d4p1.sum_sector_ids("\n".join([tc1,tc2,tc3,tc4]))


def test_answer():
    assert d4p1.sum_sector_ids(read_input_data(4)) == 185371