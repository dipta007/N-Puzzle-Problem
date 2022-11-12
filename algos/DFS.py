from config import MAX_LIMIT

class DFS:
    def __init__(self, start):
        self.start = start
        self.open = [] # INFINITE QUEUE
        self.path = []
        self.path_found = False
        self.path_cost = -1
        self.nodes_expanded = 0
    
    def solve(self):
        dist = {}
        dist[self.start] = 0

        self.open.append(self.start)

        while len(self.open) > 0:
            board = self.open.pop()
            self.nodes_expanded += 1

            if self.nodes_expanded > MAX_LIMIT:
                break

            if board.is_solved():
                self.path_found = True
                self.path_cost = board.g
                break
            for i in range(4):
                new_board = board.move(i)
                if new_board is None:
                    continue
                if new_board != board.parent:
                    self.open.append(new_board)