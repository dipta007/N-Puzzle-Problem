from queue import Queue
from config import MAX_LIMIT

class BFS:
    def __init__(self, start):
        self.start = start
        self.open = Queue(0) # INFINITE QUEUE
        self.path = []
        self.path_found = False
        self.path_cost = -1
        self.nodes_expanded = 0
    
    def solve(self):
        dist = {}
        vis = {}
        dist[self.start] = 0

        self.open.put(self.start)

        while self.open.qsize() > 0:
            board = self.open.get()
            vis[board] = True
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
                if new_board not in dist or new_board.g < dist[new_board]:
                    dist[new_board] = new_board.g
                    self.open.put(new_board)