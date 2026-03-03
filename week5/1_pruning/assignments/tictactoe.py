import itertools

from game_abstract import Game_Abstract


class TicTacToe(Game_Abstract):
    EMPTY = '-'
    PLAYERS = ['X', 'O']

    def __init__(self, size, players):
        self.size = size
        self.players = players
        for i, player in enumerate(self.players):
            player.set_value(self.PLAYERS[i])
        self.turn = 0
        self.board = [self.EMPTY] * (size * size)
        self.empty_positions = set(divmod(i, size) for i in range(size * size))

    def __repr__(self):
        s = '\n'.join(f'{i:2} ' + ' '.join(batch) 
                         for i, batch in enumerate(itertools.batched(self.board, self.size)))
        s += '\n  ' + ''.join(f'{i:2}' for i in range(self.size))
        return s
    
    def get_size(self):
        return self.size

    def get_players(self):
        return self.players

    def get_turn(self):
        return self.turn

    def get_current_player(self):
        return self.players[self.turn % len(self.players)]

    def get_possible_moves(self):
        return list(self.empty_positions)

    def __getitem__(self, move):
        return self.board[move[0] * self.size + move[1]]
    
    def __setitem__(self, move, value):
        self.board[move[0] * self.size + move[1]] = value

    def do_move(self, move, value):
        self[move] = value
        self.empty_positions.remove(move)
        self.turn += 1

    def undo_move(self, move, value):
        self[move] = self.EMPTY
        self.empty_positions.add(move)
        self.turn -= 1

    def _get_win_horizontal(self, move):
        value = self[move]
        row = move[0]
        start = row * self.size
        return self.board[start:start + self.size] == [value] * self.size

    def _get_win_vertical(self, move):
        value = self[move]
        col = move[1]
        return self.board[col: :self.size] == [value] * self.size
    
    def _get_win_diagonal(self, move):
        value = self[move]
        if move[0] == move[1]:  # main diagonal
            if self.board[0: :self.size+1] == [value] * self.size:
                return True
        if move[0] + move[1] == self.size - 1:  # anti-diagonal
            if (self.board[self.size-1:self.size*self.size-1:self.size-1] == 
                    [value] * self.size):
                return True
        return False
    
    def get_win_player(self, move):
        if (self._get_win_horizontal(move) or 
            self._get_win_vertical(move) or 
            self._get_win_diagonal(move)):
            return self.players[(self.turn - 1) % len(self.players)]
        return None

    def is_draw(self):
        return len(self.empty_positions) == 0

    def ask_move(self, player):
        while True: 
            print(f"Player {player.get_value()}'s turn. Give your move:")
            try:
                row = int(input(f"Enter row (0 to {self.size - 1}): "))
                col = int(input(f"Enter column (0 to {self.size - 1}): "))
                move = (row, col)
                return move
            except ValueError:
                pass
            print("Invalid move. Try again.")
