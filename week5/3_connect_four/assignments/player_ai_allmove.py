
import random

import utils
import player_abstract

import invocation_tree as ivt

class Player_AI_AllMove(player_abstract.Player_Abstract):

    @ivt.show
    def minimax(self, game, move, alpha=-float('inf'), beta=float('inf')):
        """ Return the minimax score for the current game state: 1 for win, 0 for draw, -1 for loss.
        This is computed by recursively evaluating all possible moves for both players using the minimax algorithm.
        """
        win_player = game.get_win_player(move)
        if win_player is not None:
            return 1 if win_player is self else -1
        if game.is_draw():
            return 0
        possible_moves = game.get_possible_moves()
        current_player = game.get_current_player()

        if self is current_player:  # maximizing player
            minimax_score = -1  # worst possible score
            for m in possible_moves:
                game.do_move(m, current_player.get_value())
                score = self.minimax(game, m)
                minimax_score = max(minimax_score, score)
                game.undo_move(m, current_player.get_value())
                if minimax_score == 1: # can't do better than this
                    break
        else:  # minimizing player
            minimax_score = 1  # best possible score
            for m in possible_moves:
                game.do_move(m, current_player.get_value())
                score = self.minimax(game, m)
                minimax_score = min(minimax_score, score)
                game.undo_move(m, current_player.get_value())
                if minimax_score == -1: # can't do worse than this
                    break

        return minimax_score

    @ivt.show
    def get_scored_moves(self, game):
        """ Returns a dictionary of each possible move as key and as value the score of the move: 1 for win, 0 for draw, -1 for loss. """
        scored_moves = {}
        possible_moves = game.get_possible_moves()
        for move in possible_moves:
            game.do_move(move, self.get_value())
            score = self.minimax(game, move)
            scored_moves[move] = score
            game.undo_move(move, self.get_value())
        return scored_moves

    @ivt.show
    def get_move(self, game):
        """ Returns the best move from the scored_moves from get_scored_moves(). """
        scored_moves = self.get_scored_moves(game)
        best_score, best_moves = utils.get_best_moves(scored_moves)
        if best_score == 1:
            print(f"Player {self.get_value()} sees it's winning.")
        return random.choice(best_moves)


