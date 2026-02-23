import pytest
import softeng

import exercise3_palindromes

def test_palindromes_is_recursive():
    assert softeng.is_recursive(exercise3_palindromes.palindromes), "The function 'palindromes()' should be recursive."

def get_lines(elements, n):
    import io
    import sys

    captured_output = io.StringIO()
    sys.stdout = captured_output
    exercise3_palindromes.palindromes(elements, '', n)
    sys.stdout = sys.__stdout__
    output = captured_output.getvalue().strip().split('\n')
    return set(output)

def test_palindromes_n1(capsys):
    lines = get_lines('ABC', 1)
    assert lines == {'A', 'B', 'C'}

def test_palindromes_n2(capsys):
    lines = get_lines('ABC', 2)
    assert lines == {'AA', 'BB', 'CC'}

def test_palindromes_n3(capsys):
    lines = get_lines('AB', 3)
    assert lines == {'AAA', 'ABA', 'BAB', 'BBB'}

def test_palindromes_n4(capsys):
    lines = get_lines('AB', 4)
    assert lines == {'AAAA', 'ABBA', 'BAAB', 'BBBB'}

def test_palindromes_n5(capsys):
    lines = get_lines('AB', 5)
    assert lines == {'AABAA', 'ABABA', 'ABBBA', 'AAAAA', 'BBABB', 'BABAB', 'BAAAB', 'BBBBB'}

def test_palindromes_n0(capsys):
    lines = get_lines('ABC', 0)
    assert lines == {''}