import argparse
import sys

from tictactoe import TicTacToe

from player_human import Player_Human
from player_random import Player_Random
from player_ai_1move import Player_AI_1Move
from player_ai_2move import Player_AI_2Move
from player_ai_allmove import Player_AI_AllMove
from player_ai_dmove import Player_AI_DMove

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-g", type=str, help="the game to play, default 'ttt'",
                        choices=["ttt"], default="ttt")
    parser.add_argument("-s", type=str, help="the size of the game",
                        default="")
    parser.add_argument("-p1", type=str,
                        help="""type of player1: 'h' (human, default), 'r' (random), 'a1' (AI 1 move), 'a2' (AI 2 moves), 'aa' (AI all moves)""", default="h")
    parser.add_argument("-p2", type=str,
                        help="""type of player2: 'h' (human), 'r' (random, default), 'a1' (AI 1 move), 'a2' (AI 2 moves), 'aa' (AI all moves)""", default="r")
    args = parser.parse_args()

    players = [player_factory(type) for type in [args.p1, args.p2]]
    game = game_factory(args.g, args.s, players)
    while game.get_possible_moves():
        print(game)
        current_player = game.get_current_player()
        move = current_player.get_move(game)
        print(f'Player {current_player.get_value()} selected move:', move)
        game.do_move(move, current_player.get_value())
        if game.get_win_player(move) is current_player:
            print(f"Player {current_player.get_value()} wins!")
            break
    else:
        print("It's a draw!")
    print(game)

def game_factory(game, size, players):
    if game == 'ttt':
        size = int(size) if size else 3
        return TicTacToe(size, players)
    else:
        print(f"Game {game} is not available.", file=sys.stderr)
        sys.exit(1)

def player_factory(player_type):
    if player_type[0] == 'd':
        if player_type[-1] == 'h':
            depth = int(player_type[1:-1])
            return Player_AI_DMove(depth, heuristic=True)
        else:
            depth = int(player_type[1:])
            return Player_AI_DMove(depth, heuristic=False)
    available_player_types = {
        'h'  : Player_Human,
        'r'  : Player_Random,
        'a1' : Player_AI_1Move,
        'a2' : Player_AI_2Move,
        'aa' : Player_AI_AllMove,
    }
    if player_type not in available_player_types:
        print(f"Player type {player_type} is not available.", file=sys.stderr)
        sys.exit(1)
    return available_player_types[player_type]()

if __name__ == "__main__":
    main()