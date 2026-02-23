import player_abstract

class Player_Human(player_abstract.Player_Abstract):

    def get_move(self, game):
        possible_moves = game.get_possible_moves()
        if not possible_moves:
            assert False, "No possible moves left"
        while True: 
            move = game.ask_move(self)
            if move in possible_moves:
                return move