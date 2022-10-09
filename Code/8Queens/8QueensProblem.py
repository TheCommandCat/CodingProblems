import numpy as np
from diagnols import isDiagnolsValid

# change the recursion limit

# import sys
# sys.setrecursionlimit()

# initialization the board
board = np.zeros((8, 8), dtype=int)

# setting the global variables 
numOfQueens = 0
PlacedQueenArray = []

# a function to find the next possible place on the board
def nextValidPlace(loc):
    y = loc[0]
    x = loc[1]
    if y != 7 and x != 7:
        return [y, x+1]
    if x == 7 and y+1 != 8:
        return [y+1, 0]
    return None

# the algorithm
def solve(board, StartFrom):
    global numOfQueens
    global PlacedQueenArray
    for i in range(StartFrom[0], 8):
        for j in range(StartFrom[1], 8):
            # checking if the place isnt already taken
            if board[i, j] != 1:
                board[i, j] = 1
                if list(board[i]).count(1) > 1 or list(board[:, j]).count(1) > 1:
                    board[i,j] = 0

                # hard diagonal part... check if the diagonal to the given spot are free 
                # TODO make it better with a diffrent search(if possible)
                if not isDiagnolsValid(board, i, j):
                    board[i, j] = 0

                # check if the spot passed all the tests above
                # if yes, adding it to the global variables
                # if not, just continuing with the for loop until we find the right spot
                if board[i, j] == 1:
                    PlacedQueenArray.append([i, j])
                    numOfQueens += 1
                
    print(numOfQueens)
    if numOfQueens != 8:
        # visualize whare we are
        print(board)

        # last place wasnt good so we are deleting it + updating the numOfQueens value
        board[PlacedQueenArray[-1][0], PlacedQueenArray[-1][1]] = 0
        numOfQueens -= 1

        # calculating the next valid place to insert a queen and setting it as the new start point
        cords = PlacedQueenArray.pop()
        startPoint = nextValidPlace([cords[0], cords[1]])
        print(startPoint)

        # if there isnt a valid place(last queen was placed in 8,8 for example)
        if startPoint == None:
            # doing the same thing as in lines 52-62 but going backwards in the PlacedQueenArray
            print(board)
            board[PlacedQueenArray[-1][0], PlacedQueenArray[-1][1]] = 0
            numOfQueens -= 1
            cords = PlacedQueenArray.pop()
            startPoint = nextValidPlace([cords[0], cords[1]])
            print(startPoint)
        solve(board, nextValidPlace([cords[0], cords[1]]))

# trigger the algorithm
solve(board, [0,0])

# prints the results when the algorithm is done(never happens)
print(board, PlacedQueenArray, numOfQueens)