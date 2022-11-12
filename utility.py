def get_heuristics(algo):
    if algo == "A_star":
        return ["manhattan", "euclidean", "hamming", "linear_conflict", None]
    elif algo == "BFS":
        return [None]
    elif algo == "DFS":
        return [None]
    elif algo == "IDDFS":
        return [None]
    elif algo == "GBFS":
        return ["manhattan", "euclidean", "hamming", "linear_conflict", None]
    elif algo == "DLS":
        return [None]
    elif algo == "UCS":
        return [None]
    else:
        return [None]