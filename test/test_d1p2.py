from d1p2 import detect_double_visit

def test_case_one():
    assert detect_double_visit("R8, R4, R4, R8") == [4, 0]