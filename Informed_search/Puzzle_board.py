import math as m

class Puzzle_board:
    def __init__(self, ls_tiles, path=None, zero_position=None):
        if path is None:
            self.path = ''
        else:
            self.path = path
        self.zero_position = zero_position
        self.board = []
        self.dimension = int(m.sqrt(len(ls_tiles)))
        for i in range(self.dimension):
            self.board.append(list())
        for i in range(len(ls_tiles)):
            self.board[int(i / self.dimension)].append(ls_tiles[i])
            if ls_tiles[i] == '0':
                self.zero_position = [int(i / self.dimension), i % self.dimension]

    def get_zero_position(self):
        return self.zero_position

    def print_board(self):
        for row in self.board:
            print(row)
        print('\n')

    def __lt__(self, other):
        return True

    def __gt__(self, other):
        return True

    def __eq__(self, other):
        return True

    def move_right(self):
        if self.zero_position[1] == 0:
            return
        else:
            zp = self.zero_position
            self.board[zp[0]][zp[1]], self.board[zp[0]][zp[1] - 1] = self.board[zp[0]][zp[1] - 1], self.board[zp[0]][
                zp[1]]
            self.zero_position[1] = self.zero_position[1] - 1
            self.path = self.path + 'R'

    def move_left(self):
        if self.zero_position[1] == self.dimension-1:
            return
        else:
            zp = self.zero_position
            self.board[zp[0]][zp[1]], self.board[zp[0]][zp[1] + 1] = self.board[zp[0]][zp[1] + 1], self.board[zp[0]][
                zp[1]]
            self.zero_position[1] = self.zero_position[1] + 1
            self.path = self.path + 'L'

    def move_up(self):
        if self.zero_position[0] == 0:
            return
        else:
            zp = self.zero_position
            self.board[zp[0]][zp[1]], self.board[zp[0] - 1][zp[1]] = self.board[zp[0] - 1][zp[1]], self.board[zp[0]][zp[1]]
            self.zero_position[0] = self.zero_position[0] - 1
            self.path = self.path + 'U'

    def move_down(self):
        if self.zero_position[0] == self.dimension-1:
            return
        else:
            zp = self.zero_position
            self.board[zp[0]][zp[1]], self.board[zp[0] + 1][zp[1]] = self.board[zp[0] + 1][zp[1]], self.board[zp[0]][
                zp[1]]
            self.zero_position[0] = self.zero_position[0] + 1
            self.path = self.path + 'D'

    def is_boards_equal(self, temp_board):    # returns true when both when passing board is equal to calling board
        flag = True
        for row1, row2 in zip(self.board, temp_board):
            for val1, val2 in zip(row1, row2):
                if val1 != val2:
                    flag = False
                    return flag
        return flag

    def get_misplaced_tiles(self, goal_state):
        count = 0
        for row1, row2 in zip(self.board, goal_state):
            for val1, val2 in zip(row1, row2):
                if val1 != val2:
                    if val1 != '0':
                        count = count +1
        return count

    def get_manhattan_distance(self,n,goal_state_ver=1):
        manhattan_dis = 0
        if goal_state_ver == 1:
            for x, row in enumerate(self.board):
                for y, val in enumerate(row):
                    if val != '0':
                        mod_x = m.fabs(x-m.floor(int(val)/n))
                        mod_y = m.fabs(y-int(val) % n)
                        manhattan_dis = manhattan_dis + mod_x + mod_y
        if goal_state_ver == 2:
            for x, row in enumerate(self.board):
                for y, val in enumerate(row):
                    if val != '0':
                        mod_x = m.fabs(x-(m.ceil((n*n-int(val))/n)-1))
                        mod_y = m.fabs(y-(n*n-1-int(val)) % n)
                        manhattan_dis = manhattan_dis + mod_x + mod_y
        return int(manhattan_dis)





