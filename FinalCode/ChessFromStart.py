import numpy as np
from diagnols import isDiagnolsValid

board = np.zeros((8, 8), dtype=int)

StartFrom = [0, 0]
global numOfQueens
numOfQueens = 0

def solve(board, StartFrom):
    global numOfQueens
    global lastQ
    for i in range(StartFrom[0], 8):
        for j in range(StartFrom[1], 8):

            if board[i, j] != 1:
                board[i, j] = 1

                if list(board[i]).count(1) > 1 or list(board[:, j]).count(1) > 1:
                    board[i,j] = 0

                # hard diagonal part...
                #TODO make it better with np diagonal
                if not isDiagnolsValid(board, i, j):
                    board[i, j] = 0

                if board[i, j] == 1:
                    lastQ = [i, j]
                    numOfQueens += 1
                    
solve(board, StartFrom)
print(board)
print(numOfQueens)