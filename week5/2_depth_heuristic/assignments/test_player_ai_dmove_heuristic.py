import pytest

from tictactoe import TicTacToe
from player_ai_dmove import Player_AI_DMove, Score
from player_ai_dmove import Score

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
        
def test_scored_moves_d0():
    players = [Player_AI_DMove(0, heuristic=True), Player_AI_DMove(0, heuristic=True)]
    game = TicTacToe(3, players)
    moves = [ ((1,1), {(0, 1): Score(0, 0, -2), (0, 0): Score(0, 0, -1), (1, 2): Score(0, 0, -2),
                       (2, 1): Score(0, 0, -2), (1, 0): Score(0, 0, -2), (2, 0): Score(0, 0, -1),
                       (0, 2): Score(0, 0, -1), (2, 2): Score(0, 0, -1)}),
              ((2,2), {(0, 1): Score(0, 0, 3), (1, 2): Score(0, 0, 3), (0, 0): Score(0, 0, 3),
                       (2, 0): Score(0, 0, 4), (1, 0): Score(0, 0, 3), (2, 1): Score(0, 0, 3),
                       (0, 2): Score(0, 0, 4)}),
              ((0,2), {(0, 1): Score(0, 0, -2), (1, 2): Score(0, 0, -3), (2, 1): Score(0, 0, -2),
                       (0, 0): Score(0, 0, -2), (2, 0): Score(0, 0, 0), (1, 0): Score(0, 0, -2)}),
              ((2,1), {(0, 1): Score(0, 0, 3), (1, 2): Score(0, 0, 3), (0, 0): Score(0, 0, 4),
                       (2, 0): Score(1, 0, 6), (1, 0): Score(0, 0, 4)}),
              ((0,1), {(1, 2): Score(0, 0, -2), (0, 0): Score(0, 0, 0), (2, 0): Score(1, 0, 1),
                       (1, 0): Score(0, 0, -1)}),
              ((1,0), {(1, 2): Score(0, 0, 1), (0, 0): Score(1, 0, 3), (2, 0): Score(1, 0, 5)}),
              ((1,2), {(0, 0): Score(0, 0, 2), (2, 0): Score(1, 0, 3)}),
              ((2,0), {(0, 0): Score(1, 0, 0)}),
        ]
    helper_test_scored_moves(players, game, moves)


def test_scored_moves_d5_draw():
    players = [Player_AI_DMove(5, heuristic=True), Player_AI_DMove(5, heuristic=True)]
    game = TicTacToe(3, players)
    moves = [ ((1,1), {(0, 1): Score(-1, 0, -4), (0, 0): Score(0, 0, -3), (1, 2): Score(-1, 0, -4),
                       (2, 1): Score(-1, 0, -4), (1, 0): Score(-1, 0, -4), (2, 0): Score(0, 0, -3),
                       (0, 2): Score(0, 0, -3), (2, 2): Score(0, 0, -3)}),
              ((2,2), {(0, 1): Score(0, 0, 0), (1, 2): Score(0, 0, 0), (0, 0): Score(0, 0, 0),
                       (2, 0): Score(0, 0, 0), (1, 0): Score(0, 0, 0), (2, 1): Score(0, 0, 0),
                       (0, 2): Score(0, 0, 0)}),
              ((0,2), {(0, 1): Score(-1, -4, -5), (1, 2): Score(-1, -4, -6), (2, 1): Score(-1, -4, -6),
                       (0, 0): Score(-1, -4, -5), (2, 0): Score(0, 0, 0), (1, 0): Score(-1, -4, -5)}),
              ((2,0), {(0, 1): Score(-1, -4, -1), (1, 2): Score(-1, -4, -1), (2, 1): Score(0, 0, 0),
                       (0, 0): Score(-1, -4, 0), (1, 0): Score(-1, -4, 0)}),
              ((2,1), {(0, 1): Score(0, 0, 0), (1, 2): Score(-1, -4, -4), (0, 0): Score(-1, -4, -2),
                       (1, 0): Score(-1, -4, -3)}),
              ((0,1), {(1, 2): Score(0, 0, 0), (0, 0): Score(0, 0, 0), (1, 0): Score(0, 0, 0)}),
              ((1,0), {(1, 2): Score(0, 0, 0), (0, 0): Score(-1, -4, -3)}),
              ((1,2), {(0, 0): Score(0, 0, 0)}),
        ]
    helper_test_scored_moves(players, game, moves)

def test_scored_moves_d5_win():
    players = [Player_AI_DMove(5, heuristic=True), Player_AI_DMove(5, heuristic=True)]
    game = TicTacToe(3, players)
    moves = [ ((1,1), {(0, 1): Score(-1, 0, -4), (0, 0): Score(0, 0, -3), (1, 2): Score(-1, 0, -4),
                       (2, 1): Score(-1, 0, -4), (1, 0): Score(-1, 0, -4), (2, 0): Score(0, 0, -3),
                       (0, 2): Score(0, 0, -3), (2, 2): Score(0, 0, -3)}),
              ((1,0), {(0, 1): Score(1, 1, 4), (1, 2): Score(0, 0, 0), (0, 0): Score(1, 1, 3),
                       (0, 2): Score(1, 1, 3), (2, 1): Score(1, 1, 4), (2, 0): Score(1, 1, 3),
                       (2, 2): Score(1, 1, 3)}),
              ((2,2), {(0, 1): Score(-1, -4, -6), (1, 2): Score(-1, -4, -7), (2, 1): Score(-1, -4, -6),
                       (0, 0): Score(-1, -2, -3), (2, 0): Score(-1, -4, -6), (0, 2): Score(-1, -4, -5)}),
              ((0,0), {(0, 1): Score(-1, -4, 0), (1, 2): Score(-1, -4, -1), (2, 1): Score(-1, -4, -1),
                       (2, 0): Score(1, 3, 3), (0, 2): Score(-1, -4, 0)}),
              ((2,0), {(0, 1): Score(-1, -4, -7), (1, 2): Score(-1, -4, -6), (2, 1): Score(-1, -4, -5),
                       (0, 2): Score(-1, -4, -3)}),
              ((0,2), {(0, 1): Score(0, 0, 0), (1, 2): Score(-1, -4, -1), (2, 1): Score(1, 5, 3)}),
              ((2,1), {(0, 1): Score(1, 5, 0), (1, 2): Score(-1, -4, -6)}),
        ]
    helper_test_scored_moves(players, game, moves)
