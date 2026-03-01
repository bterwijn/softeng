import itertools

from game_abstract import Game_Abstract
import connect_four_heuristic

class Connect_Four(Game_Abstract):
    EMPTY = '-'
    PLAYERS = ['X', 'O']
    MIN_WIN_LENGTH = 4

    def __init__(self, size, players):
        self.size = size
        self.players = players
        for i, player in enumerate(self.players):
            player.set_value(self.PLAYERS[i])
        self.turn = 0
        self.board = [self.EMPTY] * (size[0] * size[1])
        self.open_columns = set(range(size[1]))

    def __repr__(self):
        s = ''.join(f'{i:2}' for i in range(self.size[1])) + '\n'
        s += '\n'.join(' ' + ' '.join(batch) 
                         for batch in itertools.batched(self.board, self.size[1]))
        
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
        return list(self.open_columns)

    def __getitem__(self, pos):
        return self.board[pos[0] * self.size[1] + pos[1]]
    
    def __setitem__(self, pos, value):
        self.board[pos[0] * self.size[1] + pos[1]] = value

    def _column_height(self, col):
        for row in reversed(range(self.size[0])):
            if self[(row, col)] == self.EMPTY:
                return row
        return -1

    def do_move(self, move, value):
        row = self._column_height(move)
        self[(row, move)] = value
        if row == 0:
            self.open_columns.remove(move)
        self.turn += 1

    def undo_move(self, move, value):
        row = self._column_height(move) + 1
        self[(row, move)] = self.EMPTY
        if row == 0:
            self.open_columns.add(move)
        self.turn -= 1

    def _count_walk(self, value, start, delta):
        count = 0
        pos = start
        while 0 <= pos[0] < self.size[0] and 0 <= pos[1] < self.size[1]:
            if self[pos] == value:
                count += 1
                pos = (pos[0] + delta[0], pos[1] + delta[1])
            else:
                break
        return count
    
    def _get_win_horizontal(self, move):
        value = self[move]
        count = 1
        count += self._count_walk(value, (move[0], move[1]+1), (0, 1))
        count += self._count_walk(value, (move[0], move[1]-1), (0, -1))
        return count >= Connect_Four.MIN_WIN_LENGTH

    def _get_win_vertical(self, move):
        value = self[move]
        count = 1
        count += self._count_walk(value, (move[0]+1, move[1]), (1, 0))
        count += self._count_walk(value, (move[0]-1, move[1]), (-1, 0))
        return count >= Connect_Four.MIN_WIN_LENGTH
    
    def _get_win_diagonal1(self, move):
        value = self[move]
        count = 1
        count += self._count_walk(value, (move[0]+1, move[1]+1), (1, 1))
        count += self._count_walk(value, (move[0]-1, move[1]-1), (-1, -1))
        return count >= Connect_Four.MIN_WIN_LENGTH
    
    def _get_win_diagonal2(self, move):
        value = self[move]
        count = 1
        count += self._count_walk(value, (move[0]+1, move[1]-1), (1, -1))
        count += self._count_walk(value, (move[0]-1, move[1]+1), (-1, 1))
        return count >= Connect_Four.MIN_WIN_LENGTH

    def get_win_player(self, move):
        row = self._column_height(move) + 1
        pos = (row, move)
        if (self._get_win_horizontal(pos) or 
            self._get_win_vertical(pos) or 
            self._get_win_diagonal1(pos) or 
            self._get_win_diagonal2(pos)):
            return self.players[(self.turn - 1) % len(self.players)]
        return None
    
    def is_draw(self):
        return len(self.open_columns) == 0

    def ask_move(self, player):
        while True: 
            print(f"Player {player.get_value()}'s turn. Give your move:")
            try:
                col = int(input(f"Enter column (0 to {self.size[1] - 1}): "))
                return col
            except ValueError:
                pass
            print("Invalid move. Try again.")

    def get_heuristic_score(self, player):
        return connect_four_heuristic.estimate_score(self, player.get_value())