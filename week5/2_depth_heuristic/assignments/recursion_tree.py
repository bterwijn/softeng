

import tictactoe
from player_ai_dmove import Player_AI_DMove
import utils
import invocation_tree as ivt

def test():
    players = [Player_AI_DMove(1, True), Player_AI_DMove(1, True)]
    game = tictactoe.TicTacToe(4, players)
    for move in [(1,1), (1,2), (2,1), (2,0), (2,2), (2,3), (0,0),
                 (3,3), (3,2), (3,0), (0,3), (1,0)]:
        current_player = game.get_current_player()
        game.do_move(move, current_player.get_value())
        print(game)
    current_player = game.get_current_player()
    scored_moves = current_player.get_scored_moves(game)
    print(scored_moves)
    best_score, best_moves = utils.get_best_moves(scored_moves)
    game.do_move(best_moves[0], current_player.get_value())
    print(game)

ivt.decorator_tree = ivt.blocking()
test()
