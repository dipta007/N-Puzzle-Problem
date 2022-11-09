import random
import copy

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

class Board:
    def __init__(self, N, heuristic):
        self.N = N
        self.board = [[0 for _ in range(N)] for _ in range(N)]
        self.blank = (0, 0)
        self.parent = (-1, -1)
        self.heuristic = heuristic
        # f = g + h (g = cost, h = heuristic)
        self.f, self.g, self.h = 0, 0, 0
        if self.heuristic is not None:
            self.h = self.heuristic(self)
        self.f = self.g + self.h

    def is_solvable(self):
        inversions = 0
        for i in range(self.N):
            for j in range(self.N):
                if self.board[i][j] == 0:
                    continue
                for k in range(i, self.N):
                    for l in range(j, self.N):
                        if self.board[k][l] == 0:
                            continue
                        if self.board[i][j] > self.board[k][l]:
                            inversions += 1
        return inversions % 2 == 0

    def move(self, direction):
        x, y = self.blank
        new_x, new_y = x + dx[direction], y + dy[direction]
        if new_x < 0 or new_x >= self.N or new_y < 0 or new_y >= self.N:
            return None
        new_board = Board(self.N, self.heuristic)
        for i in range(self.N):
            for j in range(self.N):
                new_board.board[i][j] = self.board[i][j]
        new_board.blank = (new_x, new_y)
        new_board.board[x][y] = self.board[new_x][new_y]
        new_board.board[new_x][new_y] = 0
        new_board.g = self.g + 1
        if self.heuristic is not None:
            new_board.h = self.heuristic(new_board)
        new_board.f = new_board.g + new_board.h

        new_board.parent = (x, y)
        return new_board

    def input(self):
        for i in range(self.N):
            row = input().split()
            for j in range(self.N):
                self.board[i][j] = int(row[j])
                if self.board[i][j] == 0:
                    self.blank = (i, j)
        self.g = 0
        if self.heuristic is not None:
            self.h = self.heuristic(self)
        self.f = self.g + self.h

    def create_random(self):
        all_nums = [i for i in range(self.N * self.N)]
        random.shuffle(all_nums)
        for i in range(self.N):
            for j in range(self.N):
                self.board[i][j] = all_nums[i * self.N + j]
                if self.board[i][j] == 0:
                    self.blank = (i, j)
        self.g = 0
        if self.heuristic is not None:
            self.h = self.heuristic(self)
        self.f = self.g + self.h

    def get_goal(self):
        all_nums = [i for i in range(self.N * self.N)]
        all_nums = all_nums[1:] + [0]
        tmp_board = [[0 for _ in range(self.N)] for _ in range(self.N)]
        for i in range(self.N):
            for j in range(self.N):
                tmp_board[i][j] = all_nums[i * self.N + j]
        return tmp_board

    def is_solved(self):
        for i in range(self.N):
            for j in range(self.N):
                if self.board[i][j] != 0 and self.board[i][j] != i * self.N + j + 1:
                    return False
        return True
    
    def __str__(self):
        st = ""
        for j in range(self.N):
            st += "------"
        st += "\n"
        for i in range(self.N):
            for j in range(self.N):
                st += str(self.board[i][j]).center(5) + "|"
            st += "\n"
            for j in range(self.N):
                st += "------"
            st += "\n"
        
        st += f"G = {self.g}, H = {self.h}, F = {self.f}\n"
        
        return st
    
    def __eq__(self, other):
        for i in range(self.N):
            for j in range(self.N):
                if self.board[i][j] != other.board[i][j]:
                    return False
        return True

    def __lt__(self, other):
        if self.heuristic:
            return self.f < other.f
        else:
            return self.g < other.g

    def __hash__(self):
        return hash(str(self.board))

    def copy_from(self, other):
        self.N = other.N
        self.board = copy.deepcopy(other.board)
        self.blank = other.blank
        self.parent = other.parent
        self.g = 0
        if self.heuristic is not None:
            self.h = self.heuristic(self)
        self.f = self.g + self.h