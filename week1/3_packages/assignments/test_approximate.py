
from softeng import fixedhash, replace_fixedhash
import pytest
import approximate
import math

def test_number_of_coords():
    assert len(approximate.get_intersection_x_coords()) == 4

def check_distance(dist):
    x = list(approximate.get_intersection_x_coords())
    if not len(x) == 4:
        return False
    x.sort()
    return all([math.fabs(x[0] - (-13.8683)) < dist,
                math.fabs(x[1] - (-8.0796))  < dist,
                math.fabs(x[2] - (-3.9178))  < dist,
                math.fabs(x[3] - (2.2742))   < dist])

def test_x_coords():
    assert check_distance(0.1)

def test_x_coords_precise():
    assert check_distance(0.01)

def test_x_coords_more_precise():
    assert check_distance(0.001)
