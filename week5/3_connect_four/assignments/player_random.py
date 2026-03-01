import player_abstract
import random

class Player_Random(player_abstract.Player_Abstract):

    def get_move(self, game):
        move = random.choice(list(game.get_possible_moves()))
        return move
