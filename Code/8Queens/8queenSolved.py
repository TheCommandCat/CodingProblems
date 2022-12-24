def checkBoard(position, nextRow):
    qList = position
    positionsCopy = qList.copy()
    positionsCopy.append(nextRow)
    if len(positionsCopy) != len(set(positionsCopy)):
        return False
    # untile here it should work
    for i in range(len(positionsCopy)):
        
        for j in range(len(positionsCopy)):
            
            if i != j:
                if i - j == positionsCopy[i]-positionsCopy[j] or j-i == positionsCopy[i]-positionsCopy[j]:
                    return False


    # for i in range(len(qList)):
    #     if col - qList[i] != i+1 - len(positionsCopy) and qList[i] - col != i+1 - len(positionsCopy):
    #         return False
    return True

def solve(positions, k):
    if k == 9 : return positions
    #TODO not working
    for i in range(1, 8):
        if checkBoard(positions, i):
            positions.append(i)
            print(positions)
            if solve(positions, k+1) == ():
                positions=positions[:-1]
                break
    return ()

print(solve([], 1))