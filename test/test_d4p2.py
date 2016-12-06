import d4p2
from intrepid_calendar import read_input_data

tc1 = "aaaaa-bbb-z-y-x-123[abxyz]"
tc2 = "a-b-c-d-e-f-g-h-987[abcde]"
tc3 = "not-a-real-room-404[oarel]"
tc4 = "totally-real-room-200[decoy]"
tc5 = "qzmt-zixmtkozy-ivhz-343[zimth]"
tc6 = "abcde-abcde-1[abcde]"


def test_case_one():
    cipher_text, sector_id, checksum = d4p2.parse_room_entry(tc1)
    assert d4p2.room_validator(cipher_text, sector_id, checksum) == 123


def test_case_two():
    cipher_text, sector_id, checksum = d4p2.parse_room_entry(tc2)
    assert d4p2.room_validator(cipher_text, sector_id, checksum) == 987


def test_case_three():
    cipher_text, sector_id, checksum = d4p2.parse_room_entry(tc3)
    assert d4p2.room_validator(cipher_text, sector_id, checksum) == 404


def test_case_four():
    cipher_text, sector_id, checksum = d4p2.parse_room_entry(tc4)
    assert d4p2.room_validator(cipher_text, sector_id, checksum) == 0

def test_case_six():
    cipher_text, sector_id, _ = d4p2.parse_room_entry(tc5)
    assert d4p2.decrypt_caeser_cipher(cipher_text, sector_id) == "very encrypted name"

def test_case_custom_one():
    cipher_text, sector_id, checksum = d4p2.parse_room_entry(tc5)
    assert d4p2.room_validator(cipher_text, sector_id, checksum) == 343

def test_case_custom_two():
    cipher_text, sector_id, _ = d4p2.parse_room_entry(tc6)
    assert d4p2.decrypt_caeser_cipher(cipher_text, sector_id) == "bcdef bcdef"

def test_answer():
    assert d4p2.find_north_pole_object_storage(read_input_data(4)) == 984