from algos.A_star import A_star
from algos.BFS import BFS
from algos.DFS import DFS
from algos.Dijkstra import Dijkstra
from algos.GBFS import GBFS
from algos.IDDFS import IDDFS
from algos.IDA_star import IDA_star
from algos.HillClimbing import HillClimbing


def get_heuristics(algo):
    if algo in ['A_star', 'GBFS', "HillClimbing"]:
        return ["manhattan", "euclidean", "hamming", "linear_conflict"]
    elif algo in ['IDA_star']:
        return ["manhattan", "hamming", "linear_conflict"]
    else:
        return [None]

def get_algos(n):
    if n <= 3:
        return [BFS, DFS, Dijkstra, GBFS, A_star, IDA_star, IDDFS, HillClimbing]
    else:
        return [IDA_star, A_star, GBFS, HillClimbing]
