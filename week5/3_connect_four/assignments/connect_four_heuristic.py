from connect_four_evaluator import Connect_Four_Evaluator

def estimate_score(connect_four, player_value):
    """ Computes the heuristic score for a 'connect_four' board from the perspective of 'player_value'
    by summing the scores of all horizontal, vertical, and diagonal lines.
    """
    evaluator, height, width = get_evaluator_and_size(connect_four, player_value)
    score = 0
    score += estimate_score_horizontal(evaluator, height, width, connect_four)
    score += estimate_score_vertical(evaluator, height, width, connect_four)
    score += estimate_score_diagonal_up(evaluator, height, width, connect_four)
    score += estimate_score_diagonal_down(evaluator, height, width, connect_four)
    return score

def get_evaluator_and_size(connect_four, player_value):
    """ Returns a Connect_Four_Evaluator and size for the given 'connect_four' board and 'player_value' """
    evaluator = Connect_Four_Evaluator(connect_four.MIN_WIN_LENGTH, connect_four.EMPTY, player_value)
    height, width = connect_four.get_size()
    return evaluator, height, width

def estimate_score_horizontal(evaluator, height, width, connect_four):
    """ Logic to estimate the score for all horizontal lines on a Connect Four board. """
    score = 0
    for y in range(height):
        ds = estimate_line_score(evaluator,
                                    [connect_four[(y,i)] for i in range(width)]) # horizontal
        score += ds
    return score

def estimate_score_vertical(evaluator, height, width, connect_four):
    """ Logic to estimate the score for all vertical lines on a Connect Four board. """
    score = 0
    for x in range(width):
        score += estimate_line_score(evaluator,
                                    [connect_four[(i,x)] for i in range(height)]) # vertical
    return score

def estimate_score_diagonal_up(evaluator, height, width, connect_four):
    """ Logic to estimate the score for all diagonal-up lines on a Connect Four board. """
    score = 0
    for x in range(-(height-connect_four.MIN_WIN_LENGTH), width - connect_four.MIN_WIN_LENGTH + 1):
        y = 0
        if x < 0:
            y = -x
            x = 0
        steps = min(width - x, height - y)
        score += estimate_line_score(evaluator,
                                    [connect_four[(y+i,x+i)] for i in range(steps)]) # diagonal-up
    return score

def estimate_score_diagonal_down(evaluator, height, width, connect_four):
    """ Logic to estimate the score for all diagonal-down lines on a Connect Four board. """
    score = 0
    for x in range(-(height-connect_four.MIN_WIN_LENGTH), width - connect_four.MIN_WIN_LENGTH + 1):
        y = 0
        if x < 0:
            y = -x
            x = 0
        steps = min(width - x, height - y)
        score += estimate_line_score(evaluator,
                                    [connect_four[(y+i,width-1-x-i)] for i in range(steps)]) # diagonal-down
    return score

def estimate_line_score(evaluator, values):
    """ Returns the score for a single line of 'values' using the given 'evaluator'. """
    score = 0
    evaluator.clear()
    for value in values:
        score += evaluator.add(value)
    return score
