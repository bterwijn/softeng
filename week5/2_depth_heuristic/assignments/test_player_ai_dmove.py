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
    players = [Player_AI_DMove(0, heuristic=False), Player_AI_DMove(0, heuristic=False)]
    game = TicTacToe(3, players)
    moves = [ ((1,1), {(0, 1): Score(0, 0, 0), (0, 0): Score(0, 0, 0), (1, 2): Score(0, 0, 0),
                       (2, 1): Score(0, 0, 0), (1, 0): Score(0, 0, 0), (2, 0): Score(0, 0, 0),
                       (0, 2): Score(0, 0, 0), (2, 2): Score(0, 0, 0)}),
              ((2,2), {(0, 1): Score(0, 0, 0), (1, 2): Score(0, 0, 0), (0, 0): Score(0, 0, 0),
                       (2, 0): Score(0, 0, 0), (1, 0): Score(0, 0, 0), (2, 1): Score(0, 0, 0),
                       (0, 2): Score(0, 0, 0)}),
              ((0,2), {(0, 1): Score(0, 0, 0), (1, 2): Score(0, 0, 0), (2, 1): Score(0, 0, 0),
                       (0, 0): Score(0, 0, 0), (2, 0): Score(0, 0, 0), (1, 0): Score(0, 0, 0)}),
              ((2,1), {(0, 1): Score(0, 0, 0), (1, 2): Score(0, 0, 0), (0, 0): Score(0, 0, 0),
                       (2, 0): Score(1, 0, 0), (1, 0): Score(0, 0, 0)}),
              ((0,1), {(1, 2): Score(0, 0, 0), (0, 0): Score(0, 0, 0), (2, 0): Score(1, 0, 0),
                       (1, 0): Score(0, 0, 0)}),
              ((1,0), {(1, 2): Score(0, 0, 0), (0, 0): Score(1, 0, 0), (2, 0): Score(1, 0, 0)}),
              ((1,2), {(0, 0): Score(0, 0, 0), (2, 0): Score(1, 0, 0)}),
              ((2,0), {(0, 0): Score(1, 0, 0)}),
        ]
    helper_test_scored_moves(players, game, moves)


def test_scored_moves_d5_draw():
    players = [Player_AI_DMove(5, heuristic=False), Player_AI_DMove(5, heuristic=False)]
    game = TicTacToe(3, players)
    moves = [ ((1,1), {(0, 1): Score(-1, 0, 0), (0, 0): Score(0, 0, 0), (1, 2): Score(-1, 0, 0),
                       (2, 1): Score(-1, 0, 0), (1, 0): Score(-1, 0, 0), (2, 0): Score(0, 0, 0),
                       (0, 2): Score(0, 0, 0), (2, 2): Score(0, 0, 0)}),
              ((2,2), {(0, 1): Score(0, 0, 0), (1, 2): Score(0, 0, 0), (0, 0): Score(0, 0, 0),
                       (2, 0): Score(0, 0, 0), (1, 0): Score(0, 0, 0), (2, 1): Score(0, 0, 0),
                       (0, 2): Score(0, 0, 0)}),
              ((0,2), {(0, 1): Score(-1, -4, 0), (1, 2): Score(-1, -4, 0), (2, 1): Score(-1, -4, 0),
                       (0, 0): Score(-1, -4, 0), (2, 0): Score(0, 0, 0), (1, 0): Score(-1, -4, 0)}),
              ((2,0), {(0, 1): Score(-1, -4, 0), (1, 2): Score(-1, -4, 0), (2, 1): Score(0, 0, 0),
                       (0, 0): Score(-1, -4, 0), (1, 0): Score(-1, -4, 0)}),
              ((2,1), {(0, 1): Score(0, 0, 0), (1, 2): Score(-1, -4, 0), (0, 0): Score(-1, -4, 0),
                       (1, 0): Score(-1, -4, 0)}),
              ((0,1), {(1, 2): Score(0, 0, 0), (0, 0): Score(0, 0, 0), (1, 0): Score(0, 0, 0)}),
              ((1,0), {(1, 2): Score(0, 0, 0), (0, 0): Score(-1, -4, 0)}),
              ((1,2), {(0, 0): Score(0, 0, 0)}),
        ]
    helper_test_scored_moves(players, game, moves)

def test_scored_moves_d5_win():
    players = [Player_AI_DMove(5, heuristic=False), Player_AI_DMove(5, heuristic=False)]
    game = TicTacToe(3, players)
    moves = [ ((1,1), {(0, 1): Score(-1, 0, 0), (0, 0): Score(0, 0, 0), (1, 2): Score(-1, 0, 0),
                       (2, 1): Score(-1, 0, 0), (1, 0): Score(-1, 0, 0), (2, 0): Score(0, 0, 0),
                       (0, 2): Score(0, 0, 0), (2, 2): Score(0, 0, 0)}),
              ((1,0), {(0, 1): Score(1, 1, 0), (1, 2): Score(0, 0, 0), (0, 0): Score(1, 1, 0),
                       (0, 2): Score(1, 1, 0), (2, 1): Score(1, 1, 0), (2, 0): Score(1, 1, 0),
                       (2, 2): Score(1, 1, 0)}),
              ((2,2), {(0, 1): Score(-1, -4, 0), (1, 2): Score(-1, -4, 0), (2, 1): Score(-1, -4, 0),
                       (0, 0): Score(-1, -2, 0), (2, 0): Score(-1, -4, 0), (0, 2): Score(-1, -4, 0)}),
              ((0,0), {(0, 1): Score(-1, -4, 0), (1, 2): Score(-1, -4, 0), (2, 1): Score(-1, -4, 0),
                       (2, 0): Score(1, 3, 0), (0, 2): Score(-1, -4, 0)}),
              ((2,0), {(0, 1): Score(-1, -4, 0), (1, 2): Score(-1, -4, 0), (2, 1): Score(-1, -4, 0),
                       (0, 2): Score(-1, -4, 0)}),
              ((0,2), {(0, 1): Score(0, 0, 0), (1, 2): Score(-1, -4, 0), (2, 1): Score(1, 5, 0)}),
              ((2,1), {(0, 1): Score(1, 5, 0), (1, 2): Score(-1, -4, 0)}),
        ]
    helper_test_scored_moves(players, game, moves)
