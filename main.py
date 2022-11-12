import sys
import time
from Board import Board
from heuristics import get_heuristic
from utility import get_heuristics, get_algos

JUSTIFIED = 28

def main(N, trial):
    print(f"Number of rows/columns: {N}")
    print(f"Number of Trials: {trial}")

    loop = 0
    while loop < trial:
        print(f"Trial {loop + 1}")
        init_board = Board(N, None)
        init_board.create_random()
        # init_board.input()

        while not init_board.is_solvable():
            init_board.create_random()

        print("Initial board:")
        print(init_board)

        for algo in get_algos(N):
            print(f" {algo.__name__} ".center(int(4.25*JUSTIFIED), '-'))
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
                    print(f"Nodes expanded {solver.nodes_expanded}".center(JUSTIFIED), end=" | ")
                print("Time: ", time.time() - start_time)

            print()

        loop += 1


if __name__ == "__main__":
    N = int(sys.argv[1])
    trial = int(sys.argv[2])
    main(N, trial)