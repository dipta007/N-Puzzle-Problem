import heapq

class Dijkstra:
    def __init__(self, start):
        self.start = start
        self.open = []
        self.path = []
        self.path_found = False
        self.path_cost = -1
        self.nodes_expanded = 0
    
    def solve(self):
        dist = {}
        vis = {}
        dist[self.start] = 0

        heapq.heapify(self.open)
        heapq.heappush(self.open, self.start)

        while len(self.open) > 0:
            board = heapq.heappop(self.open)
            vis[board] = True
            self.nodes_expanded += 1
            if board.is_solved():
                self.path_found = True
                self.path_cost = board.g
                break
            for i in range(4):
                new_board = board.move(i)
                if new_board is None:
                    continue
                if new_board not in vis:
                    if new_board not in dist or new_board.g < dist[new_board]:
                        dist[new_board] = new_board.g
                        heapq.heappush(self.open, new_board)