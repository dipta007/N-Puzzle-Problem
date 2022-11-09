import time
from Board import Board
from A_star import A_star
from heuristics import get_heuristic

def run_A_star():
    N = int(input())
    init_board = Board(N, None)
    init_board.create_random()
    # init_board.input()

    while not init_board.is_solvable():
        init_board.create_random()
    print("Initial board:")
    print(init_board)

    for heuristic in ["manhattan", "euclidean", "hamming", "linear_conflict", None]:
        board = Board(N, get_heuristic(heuristic))
        board.copy_from(init_board)

        print("Heuristic: ", heuristic)
        print("Solving...")
        start_time = time.time()
        a_star = A_star(board)
        a_star.solve()

        if a_star.path_found:
            print("Path found")
            print('cost', a_star.path_cost)
        else:
            print("Path not found")
        print("Time: ", time.time() - start_time)
        print("")
        # break

if __name__ == "__main__":
    run_A_star()