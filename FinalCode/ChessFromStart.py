import numpy as np
from diagnols import isDiagnolsValid
import sys
sys.setrecursionlimit(1000000000)

board = np.zeros((8, 8), dtype=int)

StartFrom = [0, 0]
global numOfQueens
numOfQueens = 0
lastQ = []

def printif(board):
    if numOfQueens >= 8:
        print(board)
        exit()


def nextValidPlace(loc):
    y = loc[0]
    x = loc[1]
    if y != 7 and x != 7:
        return [y, x+1]
    if x == 7 and y+1 != 8:
        return [y+1, 0]
    return None

def solve(board, StartFrom):
    print(board)
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
                    lastQ.append([i, j])
                    numOfQueens += 1
                
    print(numOfQueens)
    if numOfQueens != 8:
        # TODO write better
        printif(board)
        board[lastQ[-1][0], lastQ[-1][1]] = 0
        numOfQueens -= 1
        cords = lastQ.pop()
        startPoint = nextValidPlace([cords[0], cords[1]])
        print(startPoint)
        if startPoint == None:
            printif(board)
            board[lastQ[-1][0], lastQ[-1][1]] = 0
            numOfQueens -= 1
            cords = lastQ.pop()
            startPoint = nextValidPlace([cords[0], cords[1]])
            print(startPoint)
        solve(board, nextValidPlace([cords[0], cords[1]]))

solve(board, [3,3])
print(board, lastQ, numOfQueens)

