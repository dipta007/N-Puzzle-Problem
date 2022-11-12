import time
from Board import Board
from heuristics import get_heuristic
from utility import get_heuristics
from algos.A_star import A_star
from algos.BFS import BFS
from algos.DFS import DFS
from algos.Dijkstra import Dijkstra
from algos.GBFS import GBFS

JUSTIFIED = 28

def main():
    N = int(input("Number of rows/columns: "))
    trial = int(input("Number of trials: "))
    while trial > 0:
        
        init_board = Board(N, None)
        init_board.create_random()

        while not init_board.is_solvable():
            init_board.create_random()

        print("Initial board:")
        print(init_board)

        for algo in [BFS, DFS, Dijkstra, GBFS, A_star]:
            print(f" {algo.__name__} ".center(4*JUSTIFIED, '-'))
            for heuristic in get_heuristics(algo.__name__):
                board = Board(N, get_heuristic(heuristic))
                board.copy_from(init_board)

                print(f"Heuristic: {heuristic}".ljust(JUSTIFIED), end=" | ")
                start_time = time.time()
                solver = algo(board)
                solver.solve()

                if solver.path_found:
                    print(f'Cost {solver.path_cost}'.center(JUSTIFIED), end=" | ")
                    print(f'Nodes expanded {solver.nodes_expanded}'.center(JUSTIFIED), end=" | ")
                else:
                    print("Path Not Found".center(JUSTIFIED), end=" | ")
                    print("Nodes expanded 0".center(JUSTIFIED), end=" | ")
                print("Time: ", time.time() - start_time)

            print()

        trial -= 1


if __name__ == "__main__":
    main()