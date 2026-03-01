from collections import deque

class Connect_Four_Evaluator:

    def __init__(self, maxlen, empty_value, my_value):
        self.queue = deque(maxlen=maxlen)
        self.empty_value = empty_value
        self.my_value = my_value
        self.clear()

    def __repr__(self):
        return f'Connect_Four_Evaluator(queue={list(self.queue)}, my_value_count={self.my_value_count}, opponent_value_count={self.opponent_value_count})'

    def clear(self):
        self.queue.clear()
        self.my_value_count = 0
        self.opponent_value_count = 0

    def add(self, value):
        if value != self.empty_value:
            if value == self.my_value:
                self.my_value_count += 1
            else:
                self.opponent_value_count += 1
        if len(self.queue) == self.queue.maxlen:
            removed = self.queue.popleft()
            if removed != self.empty_value:
                if removed == self.my_value:
                    self.my_value_count -= 1
                else:
                    self.opponent_value_count -= 1
        self.queue.append(value)
        score = 0
        if len(self.queue) == self.queue.maxlen:
            if self.my_value_count > 0 and self.opponent_value_count == 0:
                score = self.my_value_count
            elif self.opponent_value_count > 0 and self.my_value_count == 0:
                score = -self.opponent_value_count
        return score
