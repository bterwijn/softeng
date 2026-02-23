

import tictactoe
import player_ai_allmove as player_ai_allmove
import utils
import invocation_tree as ivt

def test():
    players = [player_ai_allmove.Player_AI_AllMove(), player_ai_allmove.Player_AI_AllMove()]
    game = tictactoe.TicTacToe(3, players)
    game.do_move((0,2), '#')
    game.do_move((2,1), '#')
    for move in [(0,0), (0,1), (1,0), (2,0)]:
        current_player = game.get_current_player()
        game.do_move(move, current_player.get_value())
        print(game)
    current_player = game.get_current_player()
    scored_moves = current_player.get_scored_moves(game)
    print(scored_moves)
    best_score, best_moves = utils.get_best_moves(scored_moves)
    game.do_move(best_moves[0], current_player.get_value())
    print(game)

ivt.decorator_tree = ivt.blocking_each_change()
#ivt.decorator_tree = ivt.debugger()  # if used in VS Code debugger
test()
