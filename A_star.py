from Board import Board
import heapq

class A_star:
    def __init__(self, start):
        self.start = start
        self.open = []
        self.path = []
        self.path_found = False
        self.path_cost = -1
    
    def solve(self):
        dist = {}
        vis = {}
        dist[self.start] = 0

        heapq.heapify(self.open)
        heapq.heappush(self.open, self.start)

        while len(self.open) > 0:
            board = heapq.heappop(self.open)
            vis[board] = True
            if board.is_solved():
                self.path_found = True
                self.path_cost = board.g
                break
            for i in range(4):
                new_board = board.move(i)
                if new_board is None:
                    continue
                if new_board not in vis:
                    if new_board not in dist or new_board.f < dist[new_board]:
                        dist[new_board] = new_board.f
                        heapq.heappush(self.open, new_board)