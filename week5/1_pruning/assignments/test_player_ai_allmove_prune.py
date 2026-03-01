import pytest

from tictactoe import TicTacToe
from player_ai_allmove import Player_AI_AllMove

# Wrap the minimax method to count calls, dirty but effective
old_minimax = Player_AI_AllMove.minimax
count_minimax_calls = 0
def counting_minimax(self, game, move, alpha=-float('inf'), beta=float('inf')):
    global count_minimax_calls
    count_minimax_calls += 1
    return old_minimax(self, game, move, alpha, beta)
Player_AI_AllMove.minimax = counting_minimax


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
    global count_minimax_calls
    count_minimax_calls = 0
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
    print(f"Minimax was called {count_minimax_calls} times.")
    assert count_minimax_calls < (10225 + 7285) // 2, "Expecting a reduction in minimax calls after pruning."
    # 10225 is without pruning, 7285 with pruning but this count is dependent on move order so we take average to be pretty safe

def test_scored_moves_board3x3_corner():
    global count_minimax_calls
    count_minimax_calls = 0
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
    print(f"Minimax was called {count_minimax_calls} times.")
    assert count_minimax_calls <  (15002 + 7800) // 2, "Expecting a reduction in minimax calls after pruning."
    # 15002 is without pruning, 7800 with pruning but this count is dependent on move order so we take average to be pretty safe
