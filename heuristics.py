import math

def get_heuristic(heuristic_name):
    if heuristic_name == "manhattan":
        return manhattan
    elif heuristic_name == "euclidean":
        return euclidean
    elif heuristic_name == "hamming":
        return hamming
    elif heuristic_name == "linear_conflict":
        return linear_conflict
    else:
        return None

def manhattan(board):
    h = 0
    for i in range(board.N):
        for j in range(board.N):
            val = board.board[i][j] - 1
            if(val==-1):
                continue

            h += abs((val//3)-i) + abs((val%3)-j)
    return h

def euclidean(board):
    h = 0
    for i in range(board.N):
        for j in range(board.N):
            val = board.board[i][j] - 1
            if(val==-1):
                continue

            h += math.sqrt((abs((val//3)-i))**2 + (abs((val%3)-j))**2)
    return h

def hamming(board):
    h = 0
    for i in range(board.N):
        for j in range(board.N):
            val = board.board[i][j] - 1
            if(val==-1):
                continue

            if(val!=i*3+j):
                h += 1
    return h

def linear_conflict(board):
    h = 0
    for i in range(board.N):
        for j in range(board.N):
            val = board.board[i][j] - 1
            if(val==-1):
                continue

            h += abs((val//3)-i) + abs((val%3)-j)
    for i in range(board.N):
        for j in range(board.N):
            val = board.board[i][j] - 1
            if(val==-1):
                continue

            if(val//3==i):
                for k in range(j+1, board.N):
                    val2 = board.board[i][k] - 1
                    if(val2==-1):
                        continue
                    if(val2//3==i and val2%3<val%3):
                        h += 2
            if(val%3==j):
                for k in range(i+1, board.N):
                    val2 = board.board[k][j] - 1
                    if(val2==-1):
                        continue
                    if(val2%3==j and val2//3<val//3):
                        h += 2
    return h