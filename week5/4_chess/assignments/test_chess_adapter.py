import pytest
import chess

from chess_adapter import Chess_Adapter
from player_random import Player_Random

def test_chess_adapter_initialization():
    players = [Player_Random(), Player_Random()]
    game = Chess_Adapter(players)
    print(game)
    assert game.get_current_player() == players[0]
    assert len(game.get_possible_moves()) == 20  # 16 pawn moves + 4 knight moves

def test_chess_adapter_make_move():
    players = [Player_Random(), Player_Random()]
    game = Chess_Adapter(players)
    move = chess.Move.from_uci('a2a4')  # Move pawn from a2 to a4
    game.do_move(move, game.get_current_player().get_value())
    print(game)
    assert move not in game.get_possible_moves()
    assert game.get_current_player() == players[1]

def test_chess_adapter_undo_move():
    players = [Player_Random(), Player_Random()]
    game = Chess_Adapter(players)
    move = chess.Move.from_uci('a2a4')  # Move pawn from a2 to a4
    current_player = game.get_current_player()
    game.do_move(move, current_player.get_value())
    print(game)
    game.undo_move(move, current_player.get_value())
    print(game)
    assert move in game.get_possible_moves()
    assert game.get_current_player() == players[0]

def test_chess_adapter_win_detection():
    players = [Player_Random(), Player_Random()]
    game = Chess_Adapter(players)
    moves = [
        chess.Move.from_uci('e2e3'),  # White
        chess.Move.from_uci('d7d6'),  # Black
        chess.Move.from_uci('f1c4'),  # White
        chess.Move.from_uci('b8c6'),  # Black 
        chess.Move.from_uci('d1f3'),  # White
        chess.Move.from_uci('g7g6'),  # Black
        chess.Move.from_uci('f3f7'),  # White
        chess.Move.from_uci('e8d7'),  # Black
        chess.Move.from_uci('c4e6'),  # White
    ]
    previous_player = None
    current_player = game.get_current_player()
    for move in moves:
        assert game.get_win_player(move) == None, "No winner yet"
        game.do_move(move, current_player.get_value())
        previous_player = current_player
        current_player = game.get_current_player()
    print(game)
    assert game.get_win_player(move) == previous_player, "White should win with checkmate"

def test_chess_adapter_draw_detection():
    players = [Player_Random(), Player_Random()]
    game = Chess_Adapter(players)
    moves = [
        chess.Move.from_uci('g1f3'),  # White
        chess.Move.from_uci('b8c6'),  # Black
        chess.Move.from_uci('f3g1'),  # White
        chess.Move.from_uci('c6b8'),  # Black 
    ]
    current_player = game.get_current_player()
    assert game.is_draw() == False, "Game should not be a draw yet"
    for _ in range(10):  # Repeat this sequence
        for move in moves:
            game.do_move(move, current_player.get_value())
            current_player = game.get_current_player()
    print(game)
    assert game.is_draw(), "Repetition should result in a draw"

def test_chess_adapter_heuristic_changes():
    players = [Player_Random(), Player_Random()]
    game = Chess_Adapter(players)
    initial_score = game.get_heuristic_score(players[0])
    move = chess.Move.from_uci('e2e4')  # Move pawn from e2 to e4
    game.do_move(move, game.get_current_player().get_value())
    new_score = game.get_heuristic_score(players[0])
    print(game)
    print(f'{new_score=}, {initial_score=}')
    assert new_score != initial_score  # Score should change after a move

def test_chess_adapter_heuristic_gets_better():
    players = [Player_Random(), Player_Random()]
    game = Chess_Adapter(players)
    initial_score = game.get_heuristic_score(players[0])
    move1 = chess.Move.from_uci('e2e4')
    game.do_move(move1, game.get_current_player().get_value())
    new_score = game.get_heuristic_score(players[0])
    print(game)
    print(f'{new_score=}, {initial_score=}')
    assert new_score > initial_score  # Score should be better for white

def test_chess_adapter_heuristic_gets_worse():
    players = [Player_Random(), Player_Random()]
    game = Chess_Adapter(players)
    initial_score = game.get_heuristic_score(players[0])
    moves = [
        chess.Move.from_uci('e2e3'),
        chess.Move.from_uci('e7e5'),
        chess.Move.from_uci('e1e2'),  # BAD move for white
    ]
    current_player = game.get_current_player()
    for move in moves:
            game.do_move(move, current_player.get_value())
            current_player = game.get_current_player()
    new_score = game.get_heuristic_score(players[0])
    print(game)
    print(f'{new_score=}, {initial_score=}')
    assert new_score < initial_score  # Score should be worse for white
