
import random

import utils
import player_abstract

import invocation_tree as ivt
#ivt.decorator_tree = ivt.blocking_each_change()

class Player_AI_2Move(player_abstract.Player_Abstract):

    @ivt.show
    def get_2move_score(self, game):
        """ Return the worst possible score for the opponent's best response move: -1 for opponent win, 0 for draw, 1 for opponent loss."""
        return 0 # all moves are a draw, incorrect, implement correct logic

    @ivt.show
    def get_scored_moves(self, game):
        """ Returns a dictionary of each possible move as key and as value the score of the move: 0 for draw, 1 for win."""
        scored_moves = {move: 0 for move in game.get_possible_moves()} # all moves are a draw, incorrect, implement correct logic
        return scored_moves

    @ivt.show
    def get_move(self, game):
        """ Returns the best move from the scored_moves from get_scored_moves(). """
        scored_moves = self.get_scored_moves(game)
        print(f'scored moves: {scored_moves}')
        best_score, best_moves = utils.get_best_moves(scored_moves)
        if best_score == 1:
            print(f"Player {self.get_value()} sees it's winning.")
        return random.choice(best_moves)
