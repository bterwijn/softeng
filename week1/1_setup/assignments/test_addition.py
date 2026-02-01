from softeng import fixedhash, replace_fixedhash
import pytest
import addition # import the add() function as 'addition.add()'

def test_add_positive():
    assert addition.add(10, 7) == 17, "add(10, 7) should return 17"
    assert addition.add(1000, 700) == 1700, "add(1000, 700) should return 1700"
    assert addition.add(0.1, 0.07) == pytest.approx(0.17), "add(0.1, 0.07) should return approximately 0.17"

def test_add_negative():
    assert addition.add(10, -7) == 3, "add(10, -7) should return 3"
    assert addition.add(1000, -700) == 300, "add(1000, -700) should return 300"
    assert addition.add(0.1, -0.07) == pytest.approx(0.03), "add(0.1, -0.07) should return approximatley 0.03"
