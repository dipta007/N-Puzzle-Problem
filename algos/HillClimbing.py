from queue import Queue

MAX_LIMIT = 1000000
DEPTH = 100

class HillClimbing:
    def __init__(self, start):
        self.start = start
        self.open = None
        self.path = []
        self.path_found = False
        self.path_cost = -1
        self.nodes_expanded = 0
    
    def solve(self):
        dist = {}
        dist[self.start] = 0

        self.open = self.start

        while True:
            if self.open == None:
                break

            self.nodes_expanded += 1
            if self.open.is_solved():
                self.path_found = True
                self.path_cost = dist[self.open]
                break

            if self.nodes_expanded > MAX_LIMIT:
                break

            mn = self.open.h
            ind = -1
            boards = Queue(0)
            boards.put(self.open)
            vis = {}
            vis[self.open] = True
            explored = 0
            while explored < DEPTH:
                now = boards.get()

                for i in range(4):
                    nxt = now.move(i)
                    if nxt == None or nxt in vis:
                        continue
                    vis[nxt] = True
                    dist[nxt] = dist[now] + 1
                    explored += 1
                    boards.put(nxt)
                    # print(mn, nxt.h)
                    if nxt.h < mn:
                        mn = nxt.h
                        ind = nxt
            
            # print(ind)
            if ind == -1:
                break
            
            nxt = ind
            self.open = nxt