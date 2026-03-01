
import random
import invocation_tree as ivt

import utils
import player_abstract

from functools import total_ordering
@total_ordering
class Score:

    def __init__(self, win, depth, heuristic):
        self.s = (win, depth, heuristic)

    def __repr__(self):
        return 'Score' + str(self.s)

    def __lt__(self, other):
        return self.s < other.s
    
    def __eq__(self, other):
        return self.s == other.s
    
    def get_win(self):
        return self.s[0]

    def worst():
        return Score(-1, -float('inf'), -float('inf'))

    def best():
        return Score( 1,  float('inf'),  float('inf'))


class Player_AI_DMove(player_abstract.Player_Abstract):

    def __init__(self, depth, heuristic=False):
        self.depth = depth
        self.heuristic = heuristic

    def get_heuristic_score(self, game):
        if not self.heuristic:
            return 0
        return game.get_heuristic_score(self)

    @ivt.show
    def minimax(self, game, move, depth, alpha, beta):
        win_player = game.get_win_player(move)
        if win_player is not None:
            if win_player is self:
                return Score(1, depth, self.get_heuristic_score(game))   # win, higher depth is better
            else:
                return Score(-1, -depth, self.get_heuristic_score(game)) # loss, lower depth is better
        possible_moves = game.get_possible_moves()
        if game.is_draw():
            return Score(0, 0, self.get_heuristic_score(game))
        if depth == 0:
            return Score(0, 0, self.get_heuristic_score(game))
        current_player = game.get_current_player()

        if self is current_player:
            combined_score = Score.worst()
            for m in possible_moves:
                game.do_move(m, current_player.get_value())
                score = self.minimax(game, m, depth - 1, alpha, beta)
                combined_score = max(combined_score, score)
                alpha = max(alpha, combined_score)
                game.undo_move(m, current_player.get_value())
                if beta <= alpha:
                    break
        else:
            combined_score = Score.best()
            for m in possible_moves:
                game.do_move(m, current_player.get_value())
                score = self.minimax(game, m, depth - 1, alpha, beta)
                combined_score = min(combined_score, score)
                beta = min(beta, combined_score)
                game.undo_move(m, current_player.get_value())
                if beta <= alpha:
                    break
        return combined_score

    @ivt.show
    def get_scored_moves(self, game):
        scored_moves = {}
        possible_moves = game.get_possible_moves()
        for move in possible_moves:
            game.do_move(move, self.get_value())
            score = self.minimax(game, move, self.depth, Score.worst(), Score.best())
            scored_moves[move] = score
            game.undo_move(move, self.get_value())
        return scored_moves

    @ivt.show
    def get_move(self, game):
        scored_moves = self.get_scored_moves(game)
        for move, score in scored_moves.items():
            print(f'move: {move} score: {score}')
        best_score, best_moves = utils.get_best_moves(scored_moves)
        if best_score.get_win() == 1:
            print(f"Player {self.get_value()} sees it's winning.")
        return random.choice(best_moves)


