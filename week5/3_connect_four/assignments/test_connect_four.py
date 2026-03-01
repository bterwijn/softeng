import pytest

from connect_four import Connect_Four
from player_random import Player_Random

def test_win_loose_board6x7():
    players = [Player_Random(), Player_Random()]
    game = Connect_Four((6, 7), players)
    moves = [
        (3, False, False),
        (3, False, False),
        (2, False, False),
        (2, False, False),
        (1, False, False),
        (0, False, False),
        (4, True, True),
        (3, False, False),
        (2, False, False),
        (3, False, False),
        (2, False, False),
        (3, False, False),
        (2, True, True),
        (1, False, False),
        (3, True, True),
        (1, False, False),
        (1, False, False),
        (1, False, False),
        (4, True, True),
        ]
    for move, win, undo in moves:
        current_player = game.get_current_player()
        game.do_move(move, current_player.get_value())
        print(game)
        win_player = game.get_win_player(move)
        if win:
            assert win_player is current_player
        else:
            assert win_player is None
        if undo:
            game.undo_move(move, current_player.get_value())
