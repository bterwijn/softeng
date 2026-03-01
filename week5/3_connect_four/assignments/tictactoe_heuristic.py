
def estimate_line_score(tictactoe, player_value, positions):
    """ Computes the line score of all 'positions' for 'player_value' on 'tictactoe' board.
    If only 'player_value' has marks in the line, the score is the number of marks of that player.
    If only the opponent has marks in the line, the score is negative the number of marks of the opponent.
    If both players have marks in the line, the score is zero.
    If the line is empty, the score is zero.
    >>> from tictactoe import TicTacToe
    >>> t = TicTacToe(3, [])
    >>> positions = [(0,0), (0,1), (0,2)]
    >>> estimate_score(t, 'X')
    0
    >>> t[(0,0)] = 'X'
    >>> estimate_score(t, 'X')
    1
    >>> t[(0,1)] = 'X'
    >>> estimate_score(t, 'X')
    2
    >>> t[(0,2)] = 'O'
    >>> estimate_score(t, 'X')
    0
    """
    score = 0
    # Implement this function to compute a line score
    return score

def estimate_score(tictactoe, player_value):
    """ Estimate the score of the current 'tictactoe' board for player_value.
    The score is computed by summing the line scores of all rows, columns and diagonals.
    A line score is positive if it favors 'player_value', negative if it favors the opponent,
    and zero if it is neutral.
    The line score is equal to the number of marks of 'player_value' in the line if the opponent has none,
    or negative of the number of marks of the opponent if 'player_value' has none.
    >>> from tictactoe import TicTacToe
    >>> t = TicTacToe(3, [])
    >>> estimate_score(t, 'X')
    0
    >>> t[(0,0)] = 'X'
    >>> estimate_score(t, 'X')
    3
    >>> t[(0,1)] = 'X'
    >>> estimate_score(t, 'X')
    5
    >>> t[(0,2)] = 'O'
    >>> estimate_score(t, 'X')
    1
    """
    score = 0
    size = tictactoe.get_size()
    for s in range(size):
        score += estimate_line_score(tictactoe, player_value,
                                        [(i,s) for i in range(size)]) # vertical
        score += estimate_line_score(tictactoe, player_value,
                                        [(s,i) for i in range(size)]) # horizontal
    score += estimate_line_score(tictactoe, player_value,
                                    [(i,i) for i in range(size)]) # diagonal1
    score += estimate_line_score(tictactoe, player_value,
                                    [(i,size-1-i) for i in range(size)]) # diagonal2
    return score
