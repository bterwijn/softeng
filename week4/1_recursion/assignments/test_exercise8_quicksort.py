import pytest
import softeng

import exercise8_quicksort

def test_quick_sort_is_recursive():
    assert softeng.is_recursive(exercise8_quicksort.quick_sort), "The function 'quick_sort()' should be recursive."

def test_quick_sort1():
    assert exercise8_quicksort.quick_sort([3, 6, 2, 8, 4, 5]) == [2, 3, 4, 5, 6, 8]
    assert exercise8_quicksort.quick_sort([]) == []
    assert exercise8_quicksort.quick_sort([10]) == [10]
    assert exercise8_quicksort.quick_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert exercise8_quicksort.quick_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert exercise8_quicksort.quick_sort([3, -1, 0, -5, 2]) == [-5, -1, 0, 2, 3]

def test_quick_sort2():
    assert exercise8_quicksort.quick_sort(
        ['apple', 'banana', 'kiwi', 'cherry'],
        key=lambda x: len(x)
    ) == ['kiwi', 'apple', 'banana', 'cherry'], """expecting ['kiwi', 'apple', 'banana', 'cherry']
    from quick_sort(['apple', 'banana', 'kiwi', 'cherry'], key=lambda x: len(x))"""
    assert exercise8_quicksort.quick_sort(
        ['apple', 'banana', 'kiwi', 'cherry'],
        key=lambda x: -len(x)
    ) == ['banana', 'cherry', 'apple', 'kiwi'], """expecting ['banana', 'cherry', 'apple', 'kiwi']
    from quick_sort(['apple', 'banana', 'kiwi', 'cherry'], key=lambda x: -len(x))"""
