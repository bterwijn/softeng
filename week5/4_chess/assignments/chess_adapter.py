import itertools

from game_abstract import Game_Abstract

import chess
import chess.svg
import chess.engine

class Chess_Adapter(Game_Abstract):
    STOCKFISH_PATH = '/usr/games/stockfish'
    PLAYERS = [chess.WHITE, chess.BLACK]

    def __init__(self, players):
        raise NotImplementedError("Implement the Chess_Adapter class based on chess_example.py")
    
    def __repr__(self):
        raise NotImplementedError("Implement the Chess_Adapter class based on chess_example.py")
    
    def get_size(self):
        raise NotImplementedError("Implement the Chess_Adapter class based on chess_example.py")
    
    def get_players(self):
        raise NotImplementedError("Implement the Chess_Adapter class based on chess_example.py")
    
    def get_turn(self):
        raise NotImplementedError("Implement the Chess_Adapter class based on chess_example.py")
    
    def get_current_player(self):
        raise NotImplementedError("Implement the Chess_Adapter class based on chess_example.py")
    
    def get_possible_moves(self):
        raise NotImplementedError("Implement the Chess_Adapter class based on chess_example.py")
    
    def __getitem__(self, move):
        raise NotImplementedError("Implement the Chess_Adapter class based on chess_example.py")
    
    def __setitem__(self, move, value):
        raise NotImplementedError("Implement the Chess_Adapter class based on chess_example.py")
    
    def do_move(self, move, value):
        raise NotImplementedError("Implement the Chess_Adapter class based on chess_example.py")
    
    def undo_move(self, move, value):
        raise NotImplementedError("Implement the Chess_Adapter class based on chess_example.py")
    
    def get_win_player(self, move):
        raise NotImplementedError("Implement the Chess_Adapter class based on chess_example.py")
    
    def is_draw(self):
        raise NotImplementedError("Implement the Chess_Adapter class based on chess_example.py")

    def ask_move(self, player):
        raise NotImplementedError("Implement the Chess_Adapter class based on chess_example.py")
    
    def get_heuristic_score(self, player):
        raise NotImplementedError("Implement the Chess_Adapter class based on chess_example.py")
    
    def __del__(self):
        # use this so that the 'self.engine' is automatically closed when this object is deleted
        # otherwise the programs and tests may hang because the engine process is still running
        if hasattr(self, 'engine'):
            if self.engine is not None:
                self.engine.quit()
                self.engine = None
