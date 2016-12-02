from d1p1 import navigate

def test_case_one():
    assert navigate("R2, L3") == 5

def test_case_two():
    assert navigate("R2, R2, R2") == 2

def test_case_three():
    assert navigate("R5, L5, R5, R3") == 12

def test_custom_case_one():
    assert navigate("R2, R2, R2, R2") == 0