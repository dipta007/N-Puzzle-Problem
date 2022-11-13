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

            h += abs((val//board.N)-i) + abs((val%board.N)-j)
    return h

def euclidean(board):
    h = 0
    for i in range(board.N):
        for j in range(board.N):
            val = board.board[i][j] - 1
            if(val==-1):
                continue

            h += math.sqrt((abs((val//board.N)-i))**2 + (abs((val%board.N)-j))**2)
    return h

def hamming(board):
    h = 0
    for i in range(board.N):
        for j in range(board.N):
            val = board.board[i][j] - 1
            if(val==-1):
                continue

            h += abs((val//board.N)-i) + abs((val%board.N)-j)
    for i in range(board.N):
        for j in range(board.N):
            val = board.board[i][j] - 1
            if(val==-1):
                continue

            if(val//board.N==i):
                for k in range(j+1, board.N):
                    val2 = board.board[i][k] - 1
                    if(val2==-1):
                        continue
                    if(val2//board.N==i and val2%board.N<val%board.N):
                        h += 2
            if(val%board.N==j):
                for k in range(i+1, board.N):
                    val2 = board.board[k][j] - 1
                    if(val2==-1):
                        continue
                    if(val2%board.N==j and val2//board.N<val//board.N):
                        h += 2
    return h

def linear_conflict(board):
    h = 0
    for i in range(board.N):
        for j in range(board.N):
            val = board.board[i][j] - 1
            if(val==-1):
                continue

            h += abs((val//board.N)-i) + abs((val%board.N)-j)
            
    for i in range(board.N):
        for j in range(board.N):
            val = board.board[i][j] - 1
            if(val==-1):
                continue

            if(val//board.N==i):
                for k in range(j+1, board.N):
                    val2 = board.board[i][k] - 1
                    if(val2==-1):
                        continue
                    if(val2//board.N==i and val2%board.N<val%board.N):
                        h += 2
            if(val%board.N==j):
                for k in range(i+1, board.N):
                    val2 = board.board[k][j] - 1
                    if(val2==-1):
                        continue
                    if(val2%board.N==j and val2//board.N<val//board.N):
                        h += 2
    return h