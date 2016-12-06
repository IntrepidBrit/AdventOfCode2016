import d6p1


def test_one():
    data = """eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar"""
    assert d6p1.jamming_error_correction(data, r=6) == "easter"
