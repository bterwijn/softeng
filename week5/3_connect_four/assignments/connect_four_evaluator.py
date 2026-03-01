from collections import deque

class Connect_Four_Evaluator:
    """ Computes the score for a line of values in a Connect Four board."""

    def __init__(self, win_length, empty_value, my_value):
        """ Initializes the Connect_Four_Evaluator that evaluates a line of values for Connect Four.
        Args:
            win_length (int): The number of consecutive pieces needed to win.
            empty_value: The value representing an empty cell.
            my_value: The value representing the player's pieces.
        """

    def __repr__(self):
        """ Returns a string representation of the Connect_Four_Evaluator."""
        return f'Connect_Four_Evaluator'

    def clear(self):
        """ Clears the evaluator's state so it can be used for a new line evaluation. """
    
    def add(self, value):
        """ Adds the next 'value' on the line to the evaluator and 
        returns the score for the current window. 
        """
        return 0
