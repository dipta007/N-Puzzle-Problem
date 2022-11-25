import sys
from Board import Board
from heuristics import get_heuristic
from utility import get_heuristics, get_algos
import time
import pickle

JUSTIFIED = 28

def create_stat():
    stat = {}
    for algo in get_algos(N):
        algo_name = algo.__name__
        stat[algo_name] = stat.get(algo_name, {})
        for heuristic in get_heuristics(algo_name):
            stat[algo_name][heuristic] = stat[algo_name].get(heuristic, {})
            for k1 in ['cost', 'nodes_expanded', 'time']:
                stat[algo_name][heuristic][k1] = stat[algo_name][heuristic].get(k1, {})
                for k2 in ['found', 'not_found', 'all']:
                    stat[algo_name][heuristic][k1][k2] = stat[algo_name][heuristic][k1].get(k2, [])
    return stat


def update_stat(stat, algo, heuristic, cost, nodes_expanded, time, path_found):
    stat[algo][heuristic]['nodes_expanded']['all'].append(nodes_expanded)
    stat[algo][heuristic]['time']['all'].append(time)
    if path_found:
        stat[algo][heuristic]['cost']['all'].append(cost)
        stat[algo][heuristic]['cost']['found'].append(cost)
        stat[algo][heuristic]['nodes_expanded']['found'].append(nodes_expanded)
        stat[algo][heuristic]['time']['found'].append(time)
    if not path_found:
        stat[algo][heuristic]['cost']['not_found'].append(cost)
        stat[algo][heuristic]['nodes_expanded']['not_found'].append(nodes_expanded)
        stat[algo][heuristic]['time']['not_found'].append(time)
    return stat


def get_stat(N):
    stat = create_stat()
    with open(f"./data/{N*N-1}puzzle.in", "r") as f:
        t = int(f.readline().strip())
        for ci in range(t):
            f.readline()

            init_board = Board(N, None)
            init_board.create_from_file(f)
            
            print(f"Case {ci+1}\nInitial board:")
            print(init_board)

            for algo in get_algos(N):
                algo_name = algo.__name__
                print(f" {algo_name} ".center(int(4.25*JUSTIFIED), '-'))
                stat[algo_name] = stat.get(algo_name, {})
                for heuristic in get_heuristics(algo_name, N):
                    stat[algo_name][heuristic] = stat[algo_name].get(heuristic, {})
                    board = Board(N, get_heuristic(heuristic))
                    board.copy_from(init_board)

                    print(f"Heuristic: {heuristic}".ljust(JUSTIFIED), end=" | ")
                    start_time = time.time()
                    solver = algo(board)
                    solver.solve()

                    output = open(f"./out/{N*N-1}puzzle_{heuristic}.out", "a")

                    if solver.path_found:
                        print(f'Cost {solver.path_cost}'.center(JUSTIFIED), end=" | ")
                        print(f'Nodes expanded {solver.nodes_expanded}'.center(JUSTIFIED), end=" | ")
                        output.write(f"{solver.path_cost}\n")

                    else:
                        print("Path Not Found".center(JUSTIFIED), end=" | ")
                        print(f"Nodes expanded {solver.nodes_expanded}".center(JUSTIFIED), end=" | ")
                        output.write(f"impossible\n")

                    time_taken = time.time() - start_time
                    print("Time: ", time_taken)
                    stat = update_stat(stat, algo_name, heuristic, solver.path_cost, solver.nodes_expanded, time_taken, solver.path_found)

                    with open(f"./out/stat_{N}.pickle", "wb") as op:
                        pickle.dump(stat, op)

                print()
    output.close()

    print(stat)


if __name__ == '__main__':
    N = int(sys.argv[1])
    get_stat(N)