import pytest

from tictactoe import TicTacToe
from player_ai_1move import Player_AI_1Move

def test_scored_moves_game1():
    players = [Player_AI_1Move(), Player_AI_1Move()]
    game = TicTacToe(3, players)
    moves = [
        ((1,1), {(0, 1): 0, (1, 2): 0, (2, 1): 0, (0, 0): 0, (2, 0): 0, (0, 2): 0, (2, 2): 0, (1, 0): 0}),
        ((0,0), {(0, 1): 0, (1, 2): 0, (2, 1): 0, (2, 0): 0, (0, 2): 0, (2, 2): 0, (1, 0): 0}),
        ((0,1), {(1, 2): 0, (2, 1): 0, (2, 0): 0, (0, 2): 0, (2, 2): 0, (1, 0): 0}),
        ((2,2), {(1, 2): 0, (2, 1): 1, (2, 0): 0, (0, 2): 0, (1, 0): 0}),
        ((1,0), {(1, 2): 0, (2, 1): 0, (2, 0): 0, (0, 2): 0}),
        ((2,1), {(1, 2): 1, (2, 0): 0, (0, 2): 0}),
        ((0,2), {(1, 2): 0, (2, 0): 1}),
        ((1,2), {(2, 0): 1}),
        ]
    current_player = game.get_current_player()
    for move, correct_scored_moves in moves:
        print('move:', move)
        game.do_move(move, current_player.get_value())
        current_player = game.get_current_player()
        print(game)
        print('current player:', current_player.get_value())
        scored_moves = current_player.get_scored_moves(game)
        print('scored_moves        :', scored_moves)
        print('correct_scored_moves:', correct_scored_moves)
        assert scored_moves == correct_scored_moves

def test_scored_moves_game2():
    players = [Player_AI_1Move(), Player_AI_1Move()]
    game = TicTacToe(3, players)
    moves = [
        ((1,1), {(0, 1): 0, (1, 2): 0, (2, 1): 0, (0, 0): 0, (2, 0): 0, (0, 2): 0, (2, 2): 0, (1, 0): 0}),
        ((2,2), {(0, 1): 0, (1, 2): 0, (2, 1): 0, (0, 0): 0, (2, 0): 0, (0, 2): 0, (1, 0): 0}),
        ((1,0), {(0, 1): 0, (1, 2): 0, (2, 1): 0, (0, 0): 0, (2, 0): 0, (0, 2): 0}),
        ((2,1), {(0, 1): 0, (1, 2): 1, (0, 0): 0, (2, 0): 0, (0, 2): 0}),
        ((0,0), {(0, 1): 0, (1, 2): 0, (2, 0): 1, (0, 2): 0}),
        ((0,1), {(1, 2): 1, (2, 0): 1, (0, 2): 0}),
        ((1,2), {(2, 0): 1, (0, 2): 0}),
        ((2,0), {(0, 2): 0}),
        ]
    current_player = game.get_current_player()
    for move, correct_scored_moves in moves:
        print('move:', move)
        game.do_move(move, current_player.get_value())
        current_player = game.get_current_player()
        print(game)
        print('current player:', current_player.get_value())
        scored_moves = current_player.get_scored_moves(game)
        print('scored_moves        :', scored_moves)
        print('correct_scored_moves:', correct_scored_moves)
        assert scored_moves == correct_scored_moves