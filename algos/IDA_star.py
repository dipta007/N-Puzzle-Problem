from config import MAX_LIMIT

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
            if t >= 35:
                break
            bound = t
    
    def search(self, board, g, bound):
        self.nodes_expanded += 1
        f = g + board.h
        if f > bound:
            return f
        
        if board.is_solved():
            self.path_found = True
            return g

        if board in self.vis and self.vis[board] <= g:
            return MAX_LIMIT
        self.vis[board] = g
        
        min = MAX_LIMIT
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