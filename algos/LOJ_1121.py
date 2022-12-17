MAX_LIMIT = 45
INF = 100000

dir = ["D", "L", "R", "U"]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def manhattan(board):
    h = 0
    for i in range(board.N):
        for j in range(board.N):
            val = board.board[i][j] - 1
            if(val==-1):
                continue

            h += abs((val//3)-i) + abs((val%3)-j)
    return h

def delta_manhattan(r, c, nr, nc, board):
    val = board.board[r][c] - 1
    val2 = board.board[nr][nc] - 1
    if(val==-1 or val2==-1):
        return 0
    return abs((val//3)-r) + abs((val%3)-c) - abs((val//3)-nr) - abs((val%3)-nc)


class Board:
    def __init__(self, N, heuristic):
        self.N = N
        self.board = [[0 for _ in range(N)] for _ in range(N)]
        self.blank = (0, 0)
        self.parent = None
        self.level = 0
        self.heuristic = heuristic
        # f = g + h (g = cost, h = heuristic)
        self.f, self.g, self.h = 0, 0, 0
        if self.heuristic is not None:
            self.h = self.heuristic(self)
        self.f = self.g + self.h
    
    def count_inversions(self):
        inversions = 0
        arr = []
        for i in range(self.N):
            for j in range(self.N):
                if self.board[i][j] != 0:
                    arr.append(self.board[i][j])
        
        for i in range(self.N * self.N-1):
            for j in range(i+1, self.N * self.N-1):
                if arr[i] > arr[j]:
                    inversions += 1
        return inversions

    def is_solvable(self):
        if self.N % 2 == 1:
            return self.count_inversions() % 2 == 0
        else:
            inversions = self.count_inversions()
            # The blank is on odd row from bottom and number of inversions is even
            if self.blank[0] % 2 == 1:
                return inversions % 2 == 0
            # The blank is on even row from bottom and number of inversions is odd
            else:
                return inversions % 2 == 1


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
            new_board.h = self.h + delta_manhattan(x, y, new_x, new_y, self)
        new_board.f = new_board.g + new_board.h

        new_board.parent = self
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
        if not isinstance(other, Board):
            return False
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
        st = ""
        for i in range(self.N):
            for j in range(self.N):
                st += str(self.board[i][j]) + "|"
            st += "$"
        return hash(st)

    # dx = [1, 0, 0, -1]
    # dy = [0, -1, 1, 0]
    def trace(self):
        now = self
        path = []
        while now.parent is not None:
            x, y = now.blank
            px, py = now.parent.blank
            if x == px:
                if y > py:
                    path.append(2)
                else:
                    path.append(1)
            else:
                if x > px:
                    path.append(0)
                else:
                    path.append(3)
            now = now.parent
        
        return path
    
    def get_path(self):
        path = self.trace()
        path.reverse()
        return path
    

class IDA_star:
    def __init__(self, start):
        self.start = start
        self.open = []
        self.path = []
        self.path_found = False
        self.path_cost = -1
        self.nodes_expanded = 0
        self.vis = {}
    
    def solve(self):
        bound = self.start.h
        while True:
            self.vis = {}
            t = self.search(self.start, 0, bound)
            if self.path_found:
                self.path_cost = t
                break
            if t > MAX_LIMIT:
                break
            bound = t
    
    def search(self, board, g, bound):
        self.nodes_expanded += 1
        f = g + board.h
        if f > bound:
            return f
        
        if board.is_solved():
            self.path_found = True
            self.path = board.get_path()
            return g

        if board in self.vis and self.vis[board] <= g:
            return INF
        self.vis[board] = g
        
        min = INF
        for i in range(4):
            new_board = board.move(i)
            if new_board is None:
                continue
            t = self.search(new_board, g + 1, bound)
            if self.path_found:
                return t
            if t < min:
                min = t
        
        return min

def main():
    t = int(input())

    for ci in range(t):
        # input()
        board = Board(4, manhattan)
        board.input()

        solver = IDA_star(board)
        solver.solve()

        # print(f"Case {ci+1}:", end=" ")
        if solver.path_found and board.is_solvable():
            # print(solver.path)
            print("".join([dir[i] for i in solver.path]))
            # print("Solvable in", solver.path_cost, "moves")
        else:
            print("This puzzle is not solvable.")
        
        


if __name__ == '__main__':
    main()
