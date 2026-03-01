
from tictactoe import TicTacToe
from player_random import Player_Random
import tictactoe_heuristic

def test_board2x2():
    players = [Player_Random(), Player_Random()]
    game = TicTacToe(2, players)
    moves = [((0,0), 3), 
             ((1,1), 0),
             ((0,1), 3),
             ((1,0), 0),
             ]
    for move, heurstic_expected in moves:
        current_player = game.get_current_player()
        game.do_move(move, current_player.get_value())
        print(f'{move=}')
        print(game)
        heurstic_score = tictactoe_heuristic.estimate_score(game, current_player.get_value())
        print(f'{heurstic_score=}')
        assert heurstic_score == heurstic_expected

def test_board3x3():
    players = [Player_Random(), Player_Random()]
    game = TicTacToe(3, players)
    moves = [((0,0), 3), 
             ((2,1), -1),
             ((0,1), 3),
             ((1,0), -1),
             ((1,1), 4),
             ((2,0), -2),
             ((2,2), 6),
             ((1,2), -5),
             ((0,2), 6),
             ]
    for move, heurstic_expected in moves:
        current_player = game.get_current_player()
        game.do_move(move, current_player.get_value())
        print(f'{move=}')
        print(game)
        heurstic_score = tictactoe_heuristic.estimate_score(game, current_player.get_value())
        print(f'{heurstic_score=} for {current_player.get_value()}')
        assert heurstic_score == heurstic_expected
