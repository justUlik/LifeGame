#Uliana Eskova

import copy

class LifeGame:
    def __init__(self, board):
        self.board = copy.deepcopy(board)
        self.height = len(self.board[0])
        self.width = len(self.board)

    def _get_neigbours(self, coord) -> int:
        arr = []
        cnt = 0
        x = coord[1]
        y = coord[0]
        for i in range(y - 1, y + 2):
            for j in range(x - 1, x + 2):
                if i >= 0 and i < self.height and j >= 0 and j < self.width:
                    if i != y or j != x:
                        if self.board[i][j] == 1:
                            cnt += 1
        return cnt

    def get_next_generation(self):
        new_board = copy.deepcopy(self.board)
        for y in range(self.height):
            for x in range(self.width):
                if new_board[y][x] == 1:
                    if self._get_neigbours((y, x)) > 3 or self._get_neigbours((y,x)) < 2:
                        new_board[y][x] = 0
                        continue
                if new_board[y][x] == 0:
                    if self._get_neigbours((y, x)) == 3:
                        new_board[y][x] = 1
                        continue
        self.board = copy.deepcopy(new_board)
        return new_board
