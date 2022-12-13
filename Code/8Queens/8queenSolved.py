
def checkBoard(position, nextRow, col):
    qList = position
    positionsCopy = qList.copy()
    positionsCopy.append(nextRow)
    if len(positionsCopy) != len(set(positionsCopy)):
        return False
    for i in range(len(qList)):
        if col - qList[i] != i - len(positionsCopy) and qList[i] - col != i - len(positionsCopy):
            return False
    return True

def solve(positions, k):
    if k == 9 : return positions

    for i in range(1, 8):
        if checkBoard(positions, i, k):
            positions.append(i)
            if solve(positions, k+1) != ():
                break
    return ()

print(solve([], 1))