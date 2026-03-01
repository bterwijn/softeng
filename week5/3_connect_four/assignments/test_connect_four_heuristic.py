import pytest

import connect_four_heuristic
from connect_four import Connect_Four
from player_random import Player_Random

def test_heuristic_empty_board():
    players = [Player_Random(), Player_Random()]
    connect_four = Connect_Four((6, 7), players)
    score_X = connect_four_heuristic.estimate_score(connect_four, 'X')
    score_O = connect_four_heuristic.estimate_score(connect_four, 'O')
    print('score_X:', score_X)
    print('score_O:', score_O)
    assert score_X == 0
    assert score_O == 0

def test_heuristic_symmetric_board():
    players = [Player_Random(), Player_Random()]
    connect_four = Connect_Four((6, 8), players)
    moves = [3, 4, 4, 3]
    for move in moves:
        current_player = connect_four.get_current_player()
        connect_four.do_move(move, current_player.get_value())
    print(connect_four)
    evaluator, height, width = connect_four_heuristic.get_evaluator_and_size(
        connect_four, current_player.get_value())
    assert connect_four_heuristic.estimate_score_horizontal(
            evaluator, height, width, connect_four) == 0
    assert connect_four_heuristic.estimate_score_vertical(
            evaluator, height, width, connect_four) == 0
    assert connect_four_heuristic.estimate_score_diagonal_up(
            evaluator, height, width, connect_four) == 0
    assert connect_four_heuristic.estimate_score_diagonal_down(
            evaluator, height, width, connect_four) == 0
    
def test_heuristic_horizontal_vertical():
    players = [Player_Random(), Player_Random()]
    connect_four = Connect_Four((6, 7), players)
    moves = [3, 3, 4, 3]
    for move in moves:
        current_player = connect_four.get_current_player()
        connect_four.do_move(move, current_player.get_value())
    print(connect_four)
    current_player = connect_four.get_current_player()
    evaluator, height, width = connect_four_heuristic.get_evaluator_and_size(
        connect_four, current_player.get_value())
    print(current_player)
    assert connect_four_heuristic.estimate_score_horizontal(
            evaluator, height, width, connect_four) == (1+2+2+2) -(1+1+1+1) -(1+1+1+1)
    assert connect_four_heuristic.estimate_score_vertical(
            evaluator, height, width, connect_four) == 1 -2 -1
    assert connect_four_heuristic.estimate_score_diagonal_up(
             evaluator, height, width, connect_four) == 1 - 1 - 3
    assert connect_four_heuristic.estimate_score_diagonal_down(
             evaluator, height, width, connect_four) == 1 - 2 - 3
    
def test_heuristic_diagonal():
    players = [Player_Random(), Player_Random()]
    connect_four = Connect_Four((6, 7), players)
    moves = [1, 2, 2, 1]
    for move in moves:
        current_player = connect_four.get_current_player()
        connect_four.do_move(move, current_player.get_value())
    print(connect_four)
    current_player = connect_four.get_current_player()
    evaluator, height, width = connect_four_heuristic.get_evaluator_and_size(
        connect_four, current_player.get_value())
    print(current_player)
    assert connect_four_heuristic.estimate_score_horizontal(
            evaluator, height, width, connect_four) == 1 - 1 
    assert connect_four_heuristic.estimate_score_vertical(
            evaluator, height, width, connect_four) == 1 - 1
    assert connect_four_heuristic.estimate_score_diagonal_up(
             evaluator, height, width, connect_four) == 1
    assert connect_four_heuristic.estimate_score_diagonal_down(
             evaluator, height, width, connect_four) == 3 - 3