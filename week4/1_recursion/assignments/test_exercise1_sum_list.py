import pytest
import softeng

import exercise1_sum_list

def test_sum_list_is_recursive():
    assert softeng.is_recursive(exercise1_sum_list.sum_list), "The function 'sum_list()' should be recursive."

def test_sum_list():
    assert exercise1_sum_list.sum_list([3, 7, 4, 9, 2]) == 25
    assert exercise1_sum_list.sum_list([]) == 0
    assert exercise1_sum_list.sum_list([10]) == 10
    assert exercise1_sum_list.sum_list([-1, 1, -1, 1]) == 0
    assert exercise1_sum_list.sum_list([0, 0, 0]) == 0
