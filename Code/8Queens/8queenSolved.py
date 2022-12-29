def checkBoard(position, nextRow):
    qList = position
    positionsCopy = qList.copy()
    positionsCopy.append(nextRow)
    if len(positionsCopy) != len(set(positionsCopy)):
        return False
    for i in range(len(positionsCopy)):
        for j in range(len(positionsCopy)):
            if i != j:
                if i - j == positionsCopy[i]-positionsCopy[j] or j-i == positionsCopy[i]-positionsCopy[j]:
                    return False
    return True

def solve(positions, k):
    if len(positions) == 8 : print('selusion found: ', positions)
    for i in range(1, 9):
        if checkBoard(positions, i):
            positions.append(i)
            if solve(positions, k+1) == ():
                positions=positions[:k-1]
    return ()

# TODO find a way to check whenever a recursion ends

solve([], 1)