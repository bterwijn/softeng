
def estimate_score(tictactoe, player_value):

    def estimate_line_score(tictactoe, player_value, positions):
        score = 0
        for pos in positions:
            if tictactoe[pos] == player_value:
                if score < 0:
                    score = 0
                    break
                score += 1
            elif tictactoe[pos] != tictactoe.EMPTY:
                if score > 0:
                    score = 0
                    break
                score -=1
        #print(f'{score=} {positions=}')
        return score

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
    
    
