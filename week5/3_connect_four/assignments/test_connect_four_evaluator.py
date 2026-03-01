import pytest

from connect_four_evaluator import Connect_Four_Evaluator

def test_connect_four_evaluator_all_me():
    evaluator = Connect_Four_Evaluator(4, '-', 'X')
    values = ['X', 'X', '-', 'X', 'X', '-', 'X', '-', '-', 'X', '-', '-', 'X']
    expected_scores = [0, 0, 0, 3, 3, 2, 3, 2, 1, 2, 1, 1, 2]
    assert len(values) == len(expected_scores)
    for i, value, in enumerate(values):
        expected_score = expected_scores[i]
        score = evaluator.add(value)
        print(evaluator)
        assert score == expected_score, f'at index {i}: expected {expected_score}, got {score}'

def test_connect_four_evaluator_all_other():
    evaluator = Connect_Four_Evaluator(4, '-', 'X')
    values = ['O', 'O', '-', 'O', 'O', '-', 'O', 'O', 'O', 'O', '-', '-', 'O']
    expected_scores = [0, 0, 0, -3, -3, -2, -3, -3, -3, -4, -3, -2, -2]
    assert len(values) == len(expected_scores)
    for i, value, in enumerate(values):
        expected_score = expected_scores[i]
        score = evaluator.add(value)
        print(evaluator)
        assert score == expected_score, f'at index {i}: expected {expected_score}, got {score}'

def test_connect_four_evaluator_mixed():
    evaluator = Connect_Four_Evaluator(4, '-', 'X')
    values = ['X', 'O', '-', 'X', 'X', '-', 'X', 'O', '-', 'O', 'O', 'O', 'X']
    expected_scores = [0, 0, 0, 0, 0, 2, 3, 0, 0, 0, -3, -3, 0]
    assert len(values) == len(expected_scores)
    for i, value, in enumerate(values):
        expected_score = expected_scores[i]
        score = evaluator.add(value)
        print(evaluator)
        assert score == expected_score, f'at index {i}: expected {expected_score}, got {score}'