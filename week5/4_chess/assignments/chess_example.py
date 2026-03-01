import itertools

import chess
import chess.svg
import chess.engine

#STOCKFISH_PATH = '/usr/games/stockfish'   # or use the path where Stockfish is installed
STOCKFISH_PATH = 'stockfish'
PLAYERS = [chess.WHITE, chess.BLACK]

def main(engine):
    board = chess.Board()
    turn = 0
    show_board(board)
    while True:
        current_player_value = PLAYERS[turn % len(PLAYERS)]
        heuristic_score = get_heuristic_score(board, current_player_value, engine)
        print(f'current heuristic score: {heuristic_score} for {print_player_value(current_player_value)}')
        move = ask_move(board, current_player_value)
        do_move(board, move)
        turn += 1
        show_board(board)
        win_player_value = get_win_player(board)
        if win_player_value is not None:
            print(f"Player {print_player_value(win_player_value)} wins!")
            break
        if is_draw(board):
            print("The game is a draw.")
            break

def print_player_value(player_value):
    return "White" if player_value == chess.WHITE else "Black"

def show_board(board, filename='chess.svg', size=600):
    print(board.unicode(borders=True, empty_square='.', invert_color=True))
    with open(filename, 'w') as file:
        file.write(chess.svg.board(board, size=size)) # create pretty image

def get_possible_moves(board):
    return list(board.legal_moves)

def ask_move(board, player_value):
    while True:
        print(f"Player {print_player_value(player_value)}'s turn.")
        print(f"Possible moves: {', '.join(move.uci() for move in board.legal_moves)}")
        move_str = input("Enter your move in UCI format (e.g., e2e4): ")
        try:
            move = chess.Move.from_uci(move_str)
            if move in get_possible_moves(board):
                return move
            else:
                print("Illegal move. Try again.")
        except ValueError:
            print("Invalid move format. Try again.")

def do_move(board, move):
    board.push(move)
    
def undo_move(board, move):
    board.pop()

def get_heuristic_score(board, player_value, engine):
    # Get static evaluation from Stockfish (depth=0)
    result = engine.analyse(board, chess.engine.Limit(depth=0))
    score = result['score']
    # Get score from the player's perspective
    if player_value == chess.WHITE:
        pov_score = score.white()
    else:
        pov_score = score.black()
    return pov_score.score() or 0

def get_win_player(board):
    # Check if the game is over after the move
    outcome = board.outcome()
    if outcome is None:
        return None
    # Return the winner based on the outcome
    if outcome.winner is None:
        return None  # Draw
    else:
        return outcome.winner

def is_draw(board):
    outcome = board.outcome()
    return outcome is not None and outcome.winner is None

if __name__ == "__main__":
    engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)
    main(engine)
    engine.quit()
