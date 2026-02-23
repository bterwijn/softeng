import pytest

from tictactoe import TicTacToe
from player_ai_allmove import Player_AI_AllMove

def helper_test_scored_moves(players, game, moves):
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
        
def test_scored_moves_board3x3_middle():
    players = [Player_AI_AllMove(), Player_AI_AllMove()]
    game = TicTacToe(3, players)
    moves = [
        ((1,1), {(0, 1): -1, (0, 0): 0, (1, 2): -1, (2, 1): -1, (1, 0): -1, (2, 0): 0, (0, 2): 0, (2, 2): 0}),
        ((2,2), {(0, 1): 0, (1, 2): 0, (0, 0): 0, (2, 0): 0, (1, 0): 0, (2, 1): 0, (0, 2): 0}),
        ((0,2), {(0, 1): -1, (1, 2): -1, (2, 1): -1, (0, 0): -1, (2, 0): 0, (1, 0): -1}),
        ((2,0), {(0, 1): -1, (1, 2): -1, (2, 1): 0, (0, 0): -1, (1, 0): -1}),
        ((2,1), {(0, 1): 0, (1, 2): -1, (0, 0): -1, (1, 0): -1}),
        ((0,1), {(1, 2): 0, (0, 0): 0, (1, 0): 0}),
        ((1,0), {(1, 2): 0, (0, 0): -1}),
        ((1,2), {(0, 0): 0}),
        ]
    helper_test_scored_moves(players, game, moves)

def test_scored_moves_board3x3_corner():
    players = [Player_AI_AllMove(), Player_AI_AllMove()]
    game = TicTacToe(3, players)
    moves = [
        ((2,2), {(0, 1): -1, (1, 2): -1, (0, 0): 0, (1, 1): 0, (2, 0): -1, (1, 0): -1, (2, 1): -1, (0, 2): -1}),
        ((0,0), {(0, 1): 0, (1, 2): 0, (1, 1): 0, (2, 0): 0, (1, 0): 0, (2, 1): 0, (0, 2): 0}),
        ((0,2), {(0, 1): -1, (1, 2): 0, (2, 1): -1, (1, 1): -1, (2, 0): -1, (1, 0): -1}),
        ((1,2), {(0, 1): -1, (2, 1): 0, (1, 1): 0, (2, 0): 0, (1, 0): 0}),
        ((2,0), {(0, 1): -1, (2, 1): 0, (1, 1): -1, (1, 0): -1}),
        ((2,1), {(0, 1): 0, (1, 1): 0, (1, 0): 0}),
        ((1,0), {(0, 1): 0, (1, 1): 0}),
        ((1,1), {(0, 1): 0}),
        ]
    helper_test_scored_moves(players, game, moves)
