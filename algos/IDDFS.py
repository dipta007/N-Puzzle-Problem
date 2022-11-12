from config import MAX_LIMIT

class IDDFS:
    def __init__(self, start):
        self.start = start
        self.path_found = False
        self.path_cost = -1
        self.nodes_expanded = 0
    
    def solve(self):
        for depth in range(30):
            self.dfs(self.start, depth, None)
            if self.path_found:
                self.path_cost = depth
                break

    def dfs(self, board, depth, prev):
        self.nodes_expanded += 1
        if depth == 0:
            if board.is_solved():
                self.path_found = True
                self.path_cost = board.g
                return True
            return False

        for i in range(4):
            new_board = board.move(i)
            if new_board is None:
                continue
            if new_board == prev:
                continue
            self.dfs(new_board, depth - 1, board)
