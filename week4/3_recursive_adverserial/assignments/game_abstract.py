from abc import ABC, abstractmethod

class Game_Abstract(ABC):
    """ Abstract base class for a two-player turn-based game. """

    @abstractmethod
    def __init__(self, size, players):
        """ Initialize the game with it's 'size' and list of two 'players'."""
        ...

    @abstractmethod
    def __repr__(self):
        """ Return a string representation of the game board. """
        ...
    
    @abstractmethod
    def get_size(self):
        """ Return the size of the game board. """
        ...

    @abstractmethod
    def get_players(self):
        """ Return the list of players. """
        ...

    @abstractmethod
    def get_turn(self):
        """ Return the current turn number. """
        ...

    @abstractmethod
    def get_current_player(self):
        """ Return the player whose turn it currently is. """
        ...

    @abstractmethod
    def get_possible_moves(self):
        """ Return a set of possible moves in the current game state. """
        ... 

    @abstractmethod
    def __getitem__(self, move):
        """ Return the value at the given move position. """
        ...
    
    @abstractmethod
    def __setitem__(self, move, value):
        """ Set the value at the given move position. """
        ...

    @abstractmethod
    def do_move(self, move, value):
        """ Execute the given move for the player with the specified value. """
        ...

    @abstractmethod
    def undo_move(self, move, value):
        """ Undo the given move for the player with the specified value. """
        ...
    
    @abstractmethod
    def get_win_player(self, move):
        """ Return the player who has won after the given move, or None if no player has won. """
        ...

    @abstractmethod
    def is_draw(self):
        """ Return True if the game is a draw, False otherwise. """
        ...
    
    @abstractmethod
    def ask_move(self, player):
        """ Ask a human player for their move. """
        ...

    def get_heuristic_score(self, player):
        """ Return a heuristic score for the given player. Default implementation returns 0. """
        return 0
