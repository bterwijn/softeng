

def get_best_moves(scored_moves):
    best_score = max(scored_moves.values())
    best_moves = [move for move, score in scored_moves.items() if score == best_score]
    return best_score, best_moves
