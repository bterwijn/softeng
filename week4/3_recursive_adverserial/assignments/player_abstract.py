from abc import ABC, abstractmethod

class Player_Abstract(ABC):
    """ Abstract base class for a player of a turn-based game. """

    def __init__(self):
        """ Initialize the player. """
        self.value = None

    def __repr__(self):
        """ Return a string representation of the player. """
        return f"Player {self.value}"

    def set_value(self, value):
        """ Set the value representing the player in the game. """
        self.value = value

    def get_value(self):
        """ Get the value representing the player in the game. """
        return self.value

    @abstractmethod
    def get_move(self, game):
        """ Get the next move from the player given the current game state. """
        ...
