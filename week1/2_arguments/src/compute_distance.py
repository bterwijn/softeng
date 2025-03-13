import math

def compute_distance(coordinate: list[float]) -> float:
    """ Returns the Euclidean distance of a 'coordinate' to the 
    origin using the Pythagoras theorem.
    """
    total = 0
    for c in coordinate:
        total += square(c)
    return math.sqrt(total)
