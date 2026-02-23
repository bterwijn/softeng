import pytest
import softeng

import exercise2_binary

def test_binary_is_recursive():
    assert softeng.is_recursive(exercise2_binary.binary), "The function 'binary()' should be recursive."

def test_binary():
    assert exercise2_binary.binary(22) == [1, 0, 1, 1, 0]
    assert exercise2_binary.binary(1) == [1]
    assert exercise2_binary.binary(8) == [1, 0, 0, 0]
    assert exercise2_binary.binary(15) == [1, 1, 1, 1]
    assert exercise2_binary.binary(255) == [1, 1, 1, 1, 1, 1, 1, 1]
    assert exercise2_binary.binary(256) == [1, 0, 0, 0, 0, 0, 0, 0, 0]
    assert exercise2_binary.binary(341) == [1, 0, 1, 0, 1, 0, 1, 0, 1]
